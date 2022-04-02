from django.urls import path
from .views import TechnicalDesignView, EconomicDesignView, ResultsView, TechnicalDesignView2

urlpatterns = [
    path("technical_design1/", TechnicalDesignView.as_view() , name="design"),
    path("technical_design2/", TechnicalDesignView2.as_view() , name="design2"),
    path("economic_design/", EconomicDesignView.as_view(), name="economic_design"),
    path("results/", ResultsView.as_view(), name="results"),
]