from django.http.response import HttpResponse
from django.shortcuts import render
from .models import News

# Create your views here.

def news(request, pk):
    request.news = News.objects.filter(pk=pk)
    return render(request, 'news.html')