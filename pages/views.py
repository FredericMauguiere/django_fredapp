from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import CatalogItem

class HomePageView(ListView):
    model = CatalogItem
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'