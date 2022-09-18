from math import ceil
from django.shortcuts import render   # ue for rendering the page like basic.hmtl etc
from django.http import HttpResponse  #use for display text


# Create your views here.
def index(request):
    return render(request,'index.html')