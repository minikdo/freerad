from django.views.generic import ListView, UpdateView, CreateView,\
    DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Radcheck


class RadListView(LoginRequiredMixin, ListView):

    model = Radcheck


class RadCreateView(LoginRequiredMixin, CreateView):

    model = Radcheck
    fields = ['username', 'attribute', 'value', 'mac', 'description']


class RadUpdateView(LoginRequiredMixin, UpdateView):

    model = Radcheck
    fields = ['username', 'attribute', 'value', 'mac', 'description']


class RadDeleteView(LoginRequiredMixin, DeleteView):

    model = Radcheck
    success_url = '/'
