from django.urls import path
from . import views

name_app = 'contact'
urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact'),

]
