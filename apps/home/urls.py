# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.conf.urls import handler404
from django.urls import path
from apps.home import views

urlpatterns = [
    # The home page
    path('', views.user_guide, name='home'),
]
