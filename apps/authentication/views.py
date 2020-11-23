from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout, login
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError


class LoginView(LoginView):
    template_name = 'authentication/login.html'


def profile(request):
    return render(request, 'authentication/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(
                username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('posts:index'))
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'authentication/register.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('posts:index'))
