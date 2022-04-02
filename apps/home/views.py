# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.views.defaults import page_not_found, permission_denied, server_error
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

# Crear 403, 404, 500
def error_403(request, exception):
    template_name = "home/403.html"
    return permission_denied(request, exception, template_name)

def error_404(request, exception):
    template_name = "home/404.html"
    return page_not_found(request, exception, template_name)

def error_500(request):
    template_name = "home/500.html"
    return server_error(request, template_name)

@login_required(login_url="/login/")
def user_guide(request):
    context = {}
    html_template = loader.get_template("home/user_guide.html")
    return HttpResponse(html_template.render(context, request))