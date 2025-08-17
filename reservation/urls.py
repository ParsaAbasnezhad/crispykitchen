from django.urls import path
from . import views

urlpatterns = [
    path("reserve/", views.reservation_create, name="reservation_create"),
    path("reserve/success/", views.reservation_success, name="reservation_success"),
]
