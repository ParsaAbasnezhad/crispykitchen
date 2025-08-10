from django.shortcuts import render, redirect
from django.views.generic import ListView, View, TemplateView

from home.models import Newsletter, TeamMember, CategoryNewsletter, Account, Event
from menu.models import Menu


class Home(ListView):
    template_name = 'home/index.html'
    model = Menu
    context_object_name = 'menu'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['news_home']= Newsletter.objects.order_by('-id')
        context['event_home']= Event.objects.order_by('-id')
        return context





class About(View):
    def get(self, request):
        team_members = TeamMember.objects.all()
        return render(request, 'home/about.html', {'team': team_members})

    def post(self, request):
        email = request.POST.get('email')
        Account.objects.create(email=email)
        return redirect('news')


class NewsletterOrEventView(ListView):
    model = Newsletter
    context_object_name = 'newses'
    template_name = 'home/news.html'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['event_news']= Event.objects.order_by('-id')
        return context

