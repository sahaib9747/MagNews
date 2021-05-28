from django.http.response import HttpResponse
from django.shortcuts import render
from .models import News

# Create your views here.

def news(request, word):
    request.news = News.objects.filter(title=word)
    return render(request, 'front/news.html')