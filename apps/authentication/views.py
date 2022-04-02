# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from .forms import LoginForm, SignUpForm
from django import forms

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'
    return render(request, "accounts/login.html", {"form": form, "msg": msg})

def register_user(request):
    msg = None
    success = False
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()
    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

class PassResetView(PasswordResetView):
    template_name = "accounts/reset.html"
    
    def get_form(self, form_class=None):
        form = super(PassResetView, self).get_form()
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'})
        return form

class PassResetDoneView(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"

class PassResetConfirmView(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    
    def get_form(self, form_class=None):
        form = super(PassResetConfirmView, self).get_form()
        form.fields['new_password1'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'New password'})
        form.fields['new_password2'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'New password confirmation'})
        return form

class PassResetCompleteView(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"

class PassChangeView(PasswordChangeView):
    template_name = "accounts/password_change.html"

    def get_form(self, form_class=None):
        form = super(PassChangeView, self).get_form()
        form.fields['old_password'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Old password'})
        form.fields['new_password1'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'New password'})
        form.fields['new_password2'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'New password confirmation'})
        return form

class PassChangeDoneView(PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"