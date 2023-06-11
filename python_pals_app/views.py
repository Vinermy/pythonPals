from django import forms
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpRequest
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, ProfileRegistrationForm
from .models import Profile


# Create your views here.

def signup(request: HttpRequest):
    if request.method == 'POST':
        u_form = UserRegistrationForm(request.POST)
        p_form = ProfileRegistrationForm(request.POST)

        if not u_form.is_valid():
            message_form_errors(request, u_form)
            return redirect('signup')

        if not p_form.is_valid():
            message_form_errors(request, p_form)
            return redirect('signup')

        user = u_form.save()
        profile = p_form.save(commit=False)
        profile.user = user
        profile.save()
        login(request, user)
        return redirect('profile-page', user.id)

    return render(request, 'auth/signup.html')


def profile_page(request: HttpRequest, pk: int):
    context = {
        'profile': Profile.objects.get(user_id=pk)
    }
    return render(request, 'profile-page.html', context)


def message_form_errors(request: HttpRequest, form: forms.BaseForm):
    for field in form.fields:
        for error in field.errors:
            messages.WARNING(request, error)
