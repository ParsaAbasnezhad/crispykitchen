from django.shortcuts import render
from django.views.generic import TemplateView ,ListView

from menu.models import *


class MenuView(ListView):
    model = Menu
    template_name = 'menu/menu.html'
    context_object_name = 'food'

