from django.urls import path

from . import views


urlpatterns = [
    path('', views.RadListView.as_view(), name='index'),
]
