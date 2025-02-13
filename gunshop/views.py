from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
        'title': 'Welcome to Our Website!',
    }
    return render(request, 'home.html', context)