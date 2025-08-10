from django.shortcuts import render, redirect
from django.views.generic import ListView, View

from home.models import *
from menu.models import Menu


class Home(ListView):
    template_name = 'home/index.html'
    model = Menu
    context_object_name = 'menu'


class About(View):
    def get(self, request):
        team_members = TeamMember.objects.all()
        return render(request, 'home/about.html', {'team': team_members})

    def post(self, request):
        if request.method == 'POST':
            email = request.POST.get('email')
            Newsletter.objects.create(email=email)
            return redirect('home/news.html')

        return render(request, 'home/about.html')
