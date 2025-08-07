from django.shortcuts import render
from django.views.generic import TemplateView


class Menu(TemplateView):
    template_name = 'menu/menu.html'
