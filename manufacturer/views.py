# from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import ManuBsn, ManuAccount
from .forms import ManuBsnForm, ManuAccountForm

class ManuBsnCreateView(CreateView):
    model = ManuBsn
    form_class = ManuBsnForm
    template_name = 'manufacturer/manubsn_form.html'
    success_url = reverse_lazy('manubsn_list')

class ManuBsnUpdateView(UpdateView):
    model = ManuBsn
    form_class = ManuBsnForm
    template_name = 'manufacturer/manubsn_form.html'
    success_url = reverse_lazy('manubsn_list')

class ManuBsnDeleteView(DeleteView):
    model = ManuBsn
    template_name = 'manufacturer/manubsn_confirm_delete.html'
    success_url = reverse_lazy('manubsn_list')

class ManuBsnDetailView(DetailView):
    model = ManuBsn
    template_name = 'manufacturer/manubsn_detail.html'

class ManuAccountCreateView(CreateView):
    model = ManuAccount
    form_class = ManuAccountForm
    template_name = 'manufacturer/manuaccount_form.html'
    success_url = reverse_lazy('manuaccount_list')

class ManuAccountUpdateView(UpdateView):
    model = ManuAccount
    form_class = ManuAccountForm
    template_name = 'manufacturer/manuaccount_form.html'
    success_url = reverse_lazy('manuaccount_list')

class ManuAccountDeleteView(DeleteView):
    model = ManuAccount
    template_name = 'manufacturer/manuaccount_confirm_delete.html'
    success_url = reverse_lazy('manuaccount_list')

class ManuAccountDetailView(DetailView):
    model = ManuAccount
    template_name = 'manufacturer/manuaccount_detail.html'
