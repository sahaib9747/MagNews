from django.http.response import HttpResponse
from django.shortcuts import render
from .models import News

# Create your views here.

def news(request, word):
    request.news = News.objects.filter(title=word)
    return render(request, 'front/news.html')


def news_list(request):
    request.news = News.objects.all()

    return render(request, 'back/news_list.html')