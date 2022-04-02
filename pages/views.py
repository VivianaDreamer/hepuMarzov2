from django.views.generic.list import ListView
from .models import Pages

# Create your views here.
class TermsListView(ListView):
    model = Pages
    template_name = "pages/terms.html"