from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import JsonResponse
import random

i = 0
def get_i():
    global i
    i += 1
    return i

class MainView(TemplateView):
    template_name = 'pests/index.html'

class PointApiView(View):
    i = 0
    def get(self, request):
        points = []
        latmin = 43.076149
        latmax = 43.168864
        longmin = -80.125481
        longmax = -79.930081
        self.i += 1
        return JsonResponse({
            'points': get_i(),
        })

# Create your views here.
