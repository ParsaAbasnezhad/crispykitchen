from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Reservation, ReservationItem
from .forms import ReservationForm, ReservationItemForm
from menu.models import Menu
def reservation_create(request):
    ItemFormSet = modelformset_factory(ReservationItem, form=ReservationItemForm, extra=2)

    if request.method == "POST":
        form = ReservationForm(request.POST)
        formset = ItemFormSet(request.POST, queryset=ReservationItem.objects.none())

        if form.is_valid() and formset.is_valid():
            reservation = form.save()

            items = formset.save(commit=False)
            for item in items:
                item.reservation = reservation
                item.save()

            return redirect("reservation_success")

    else:
        form = ReservationForm()
        formset = ItemFormSet(queryset=Menu.objects.none())

    return render(request, "reservation/reservation_form.html", {"form": form, "formset": formset})


def reservation_success(request):
    return render(request, "reservation/reservation_success.html")
