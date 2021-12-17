from django.shortcuts import render, redirect
from .models import *

async def index(request):
    data1 = Posting.objects.all()
    data2 = Posting.objects.filter(status='Trending')
    listing = {'data1': data1, 'data2': data2}
    return render(request, 'index.html', listing)

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')