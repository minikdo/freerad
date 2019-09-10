from django.views.generic import ListView, UpdateView, CreateView,\
    DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Radcheck
from .mixins import CreatedByMixin


class RadListView(LoginRequiredMixin, ListView):

    model = Radcheck
    ordering = ['id']


class RadCreateView(LoginRequiredMixin, CreatedByMixin, CreateView):

    model = Radcheck
    fields = ['username', 'attribute', 'value', 'mac', 'description']


class RadUpdateView(LoginRequiredMixin, CreatedByMixin, UpdateView):

    model = Radcheck
    fields = ['username', 'attribute', 'value', 'mac', 'description']


class RadDeleteView(LoginRequiredMixin, DeleteView):

    model = Radcheck
    success_url = '/'
