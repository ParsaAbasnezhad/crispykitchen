from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from contact.forms import ContactForm
from contact.models import Weekday


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['weekday'] = Weekday.objects.order_by('-id').first()
        return context

