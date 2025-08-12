from django.shortcuts import render
from django.views.generic import ListView

from menu.models import Menu


class MenuView(ListView):
    model = Menu
    template_name = 'menu/menu.html'
    context_object_name = 'food'

