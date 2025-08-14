from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View

from home.models import Newsletter, TeamMember
from menu.models import Menu, Category, Comment
from .forms import CommentForm


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
