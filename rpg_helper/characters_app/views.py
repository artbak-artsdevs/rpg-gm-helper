from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Character
from .templates import *


# Create your views here.

def main_page(request):

    characters = Character.objects.all()

    context = {'chars': characters}

    return render(request, 'index.html', context=context )
