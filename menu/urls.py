from django.urls import path
from . import views


app_name = 'menu'
urlpatterns = [
    path('menu/', views.MenuView.as_view(), name='home'),
    path('detail/', views.MenuDetailView.as_view(), name='detail'),
]
