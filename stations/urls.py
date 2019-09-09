from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'stations'

urlpatterns = [
    path('', views.RadListView.as_view(), name='index'),
    path('add/', views.RadCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.RadUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.RadDeleteView.as_view(), name='delete'),

    # login
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
