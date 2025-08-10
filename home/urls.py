from django.urls import path
from .views import Home, NewsletterOrEventView, About

name_app = 'home'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('news/', NewsletterOrEventView.as_view(), name='news'),
    path('about/', About.as_view(), name='about'),
]
