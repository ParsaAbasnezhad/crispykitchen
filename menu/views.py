from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from menu.models import Menu, Category, Comment
from .forms import CommentForm


class MenuView(ListView):
    model = Menu
    template_name = 'menu/menu.html'
    context_object_name = 'food'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'menu/detail_category.html'
    context_object_name = 'category'
    pk_url_kwarg = 'id'




class CommentView(View):
    template_name = 'include/comment.html'

    def get(self, request, *args, **kwargs):
        comments = Comment.objects.all().order_by('-date')
        form = CommentForm()
        return render(request, self.template_name, {'comments': comments, 'form': form})

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        comments = Comment.objects.all().order_by('-date')

        if form.is_valid():
            form.save()
            return redirect('about')

        return render(request, self.template_name, {'comments': comments, 'form': form})
