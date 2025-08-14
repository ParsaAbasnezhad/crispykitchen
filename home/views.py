from django.shortcuts import render, redirect
from django.views.generic import ListView, View

from home.models import Newsletter, TeamMember, Event
from menu.models import Menu


class Home(ListView):
    template_name = 'home/index.html'
    model = Menu
    context_object_name = 'menu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_home'] = Newsletter.objects.order_by('id')
        context['event_home'] = Event.objects.order_by('id')
        return context


class AboutView(View):
    template_name = 'home/about.html'

    def get(self, request):
        team = TeamMember.objects.all()
        return render(request, self.template_name, {'team': team})

    def post(self, request):
        email = request.POST.get('email')
        team = TeamMember.objects.all()
        if email:
            request.session['user_email'] = email
            return redirect('news')
        else:
            error = 'email not found'
            return render(request, self.template_name, {'error': error, 'team': team})


def news_view(request):
    email = request.session.get('user_email')
    if not email:
        return redirect('about')

    news_list = Newsletter.objects.all().order_by('-id')
    events_list = Event.objects.all().order_by('-id')

    return render(request, 'home/news.html', {
        'news': news_list,
        'event': events_list
    })
