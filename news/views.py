from django.http.response import HttpResponse
from django.shortcuts import render
from .models import News

# Create your views here.

def news(request):
    return render(request, 'news.html')