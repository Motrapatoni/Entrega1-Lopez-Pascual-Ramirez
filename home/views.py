from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
#from models import *

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')
