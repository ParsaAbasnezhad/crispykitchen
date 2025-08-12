from django.urls import path

from contact.models import Contact
from .views import Home, AboutView,news_view

name_app = 'home'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('news/', news_view, name='news'),
]
