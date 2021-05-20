from django.urls import path
from . import views

app_name = "authentication"
urlpatterns = [
    path('auth/login', views.login, name='login'),
    path('auth/logout', views.logout, name='logout'),
    path('auth/register', views.register, name='register'),
]