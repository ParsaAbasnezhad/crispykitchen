from django.urls import path
from . import views

app_name = 'menu'
urlpatterns = [
    path('menu/', views.MenuView.as_view(), name='home'),
    path('detail/<int:id>/', views.CategoryDetailView.as_view(), name='detail'),
]
