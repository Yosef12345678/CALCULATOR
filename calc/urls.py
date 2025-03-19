from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('profile/', views.profile, name='profile'),  # Profile page
]