from django.shortcuts import render
from django.views.generic import TemplateView

class MainView(TemplateView):
    template_name = 'pests/index.html'

# Create your views here.
