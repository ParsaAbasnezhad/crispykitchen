from django import forms
from .models import Reservation, ReservationItem


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["customer_name", "customer_phone", "customer_email", "table", "start_time", "end_time",
                  "service_type", "address", "note"]
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_email': forms.TextInput(attrs={'class': 'form-control'}),
            'table': forms.Select(attrs={'class': 'form-control'}),
            'start_time': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'start_time'}),
            'end_time': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'end_time'}),
            'service_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'service_type'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'address'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'note'}),
        }


class ReservationItemForm(forms.ModelForm):
    class Meta:
        model = ReservationItem
        fields = ["food", "quantity"]
