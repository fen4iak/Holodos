from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='reg'),
    path('login/', LoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
]