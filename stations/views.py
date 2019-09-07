from django.views.generic import ListView

from .models import Radcheck


class RadListView(ListView):

    model = Radcheck
