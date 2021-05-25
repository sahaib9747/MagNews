from django.shortcuts import render
from .models import Appearence
from news.models import News


# Create your views here.
def home(request):
    request.page = Appearence.objects.get(title__startswith='Home')
    request.news = News.objects.all()

    return render(request, 'index.html')

def about(request):
    request.page = Appearence.objects.get(title__startswith='About')

    return render(request, 'about.html')


def base(request):
    return render(request, 'base.html')