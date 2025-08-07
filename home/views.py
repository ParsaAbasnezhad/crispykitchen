from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from menu.models import Menu


class Home(ListView):
    template_name = 'home/index.html'
    model = Menu
    context_object_name = 'menu'

