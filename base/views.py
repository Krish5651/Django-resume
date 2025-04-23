from django.shortcuts import render
import os

def home(request):
    return render(request, 'base/home.html')
