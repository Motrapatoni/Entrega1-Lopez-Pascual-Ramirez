from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
#from models import *

# Create your views here.
def items(request):
    return render(request, 'items/items.html')