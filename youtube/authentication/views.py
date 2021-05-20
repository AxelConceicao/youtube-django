from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate 
from django.contrib.auth.forms import AuthenticationForm

def logout(request):
  auth_logout(request)
  return redirect('video:index')

def login(request):
  if request.user.is_authenticated:
    return redirect('video:index')
  if request.method == "POST":
    my_form = AuthenticationForm(request, data=request.POST)
    if my_form.is_valid():
      username = my_form.cleaned_data.get('username')
      password = my_form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        auth_login(request, user)
        return redirect('video:index')
  else:
    my_form = AuthenticationForm()
  context = {
    "form": my_form,
  }
  return render(request, "login.html", context)

def register(request):
  if request.user.is_authenticated:
    return redirect('video:index')
  if request.method == "POST":
    my_form = forms.RegisterForm(request.POST)
    if my_form.is_valid():
      user = my_form.save()
      auth_login(request, user)
      return redirect('video:index')
  else:
    my_form = forms.RegisterForm
  context = {
    "form": my_form,
  }
  return render(request, "register.html", context)