from django.urls import path, re_path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('news/<int:pk>', views.news, name='news'),
]