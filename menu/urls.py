from django.urls import path
from . import views

app_name = 'menu'
urlpatterns = [
    path('menu/', views.MenuView.as_view(), name='home'),
    path('detail/<slug:slug>/', views.NewsDetailView.as_view(),name='detail' ),
    path('', views.index, name='index'),
    path('rate_menu/<int:pk>/', views.rate_menu, name='rate_menu'),

]
