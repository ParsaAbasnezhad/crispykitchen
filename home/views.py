from django.shortcuts import render, redirect
from django.views.generic import ListView, View, TemplateView

from home.models import Newsletter, TeamMember, CategoryNewsletter
from menu.models import Menu


class Home(ListView):
    template_name = 'home/index.html'
    model = Menu
    context_object_name = 'menu'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['news_home']= Newsletter.objects.order_by('-id')
        return context





class About(View):
    def get(self, request):
        team_members = TeamMember.objects.all()
        return render(request, 'home/about.html', {'team': team_members})

    def post(self, request):
        email = request.POST.get('email')
        Newsletter.objects.create(email=email)
        return redirect('news')


class NewsletterView(ListView):
    model = Newsletter
    context_object_name = 'newses'
    template_name = 'home/news.html'

