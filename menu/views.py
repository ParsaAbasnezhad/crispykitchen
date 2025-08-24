from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import Rating
from home.models import Newsletter, TeamMember
from menu.models import Menu, Category, Comment
from .forms import CommentForm, RatingForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Menu, Rating


class MenuView(ListView):
    model = Menu
    template_name = 'menu/menu.html'
    context_object_name = 'food'


class NewsDetailView(DetailView):
    model = Newsletter
    template_name = 'menu/detail_news.html'
    context_object_name = 'newsletter'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all().order_by('-date')
        context['team'] = TeamMember.objects.all()
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


def index(request):
    menus = Menu.objects.all()

    if request.method == "POST":
        menu_id = request.POST.get("menu_id")
        menu = get_object_or_404(Menu, id=menu_id)

        session_key = f"rated_{menu_id}"
        if not request.session.get(session_key):
            form = RatingForm(request.POST)
            if form.is_valid():
                rating = form.save(commit=False)
                rating.menu = menu
                rating.save()
                request.session[session_key] = True
                return redirect("index")

    context = {"menus": menus}
    return render(request, "home/index.html", context)


@csrf_exempt
def rate_menu(request, pk):
    if request.method == "POST":
        menu = Menu.objects.get(id=pk)
        value = int(request.POST.get("value"))

        session_key = f"rated_{pk}"
        if request.session.get(session_key):
            return JsonResponse({"error": "شما قبلاً رأی داده‌اید!"}, status=400)

        Rating.objects.create(menu=menu, value=value)
        request.session[session_key] = True

        return JsonResponse({"success": True, "average": menu.average_rating()})
