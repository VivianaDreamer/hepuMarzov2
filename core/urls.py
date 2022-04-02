# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    # Django admin route
    path('admin/', admin.site.urls),
    # Auth routes - login / register
    path("", include("apps.authentication.urls")),
    # Design routes
    path("design/", include("design.urls")),
    # Pages paths
    path("terms/", include("pages.urls")),
    # UI Kits Html files
    path("", include("apps.home.urls")),
]

# Error handlers
handler403 = "apps.home.views.error_403"
handler404 = "apps.home.views.error_404"
handler500 = "apps.home.views.error_500"