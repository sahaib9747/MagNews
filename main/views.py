from django.shortcuts import render
from .models import Appearence
from news.models import News


# Create your views here.
def home(request):
    request.page = Appearence.objects.get(title__startswith='Home')
    request.news = News.objects.all()

    return render(request, 'front/index.html')

def about(request):
    request.page = Appearence.objects.get(title__startswith='About')

    return render(request, 'front/about.html')


def base(request):
    return render(request, 'front/base.html')


def panel(request):
    return render(request, 'back/index.html')