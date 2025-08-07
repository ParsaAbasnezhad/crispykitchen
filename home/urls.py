from django.urls import path

from home.views import Home

name_app = 'home'
urlpatterns = [
    path('', Home.as_view(), name='home'),
]
