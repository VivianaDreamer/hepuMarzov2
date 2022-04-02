from django.urls import path
from .views import TermsListView

urlpatterns = [
    path('', TermsListView.as_view(), name="terms"),
]