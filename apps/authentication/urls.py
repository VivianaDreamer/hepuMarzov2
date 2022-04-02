# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, PassResetView, PassResetDoneView, PassResetConfirmView, PassResetCompleteView, PassChangeView, PassChangeDoneView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("reset/", PassResetView.as_view(), name="password_reset"),
    path("reset/done/", PassResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", PassResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/complete/", PassResetCompleteView.as_view(), name="password_reset_complete"),
    path('pass_change/', PassChangeView.as_view(), name="password_change"),
    path('pass_change_done/', PassChangeDoneView.as_view(), name="password_change_done"),
]
