from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
#from ... import users.templates

class HomePageView(TemplateView):
    template_name = 'home.html'
#    template_name = 'index.html'
