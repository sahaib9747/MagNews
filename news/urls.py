from django.urls import path, re_path
from . import views
from django.conf.urls import url

urlpatterns = [
    re_path(r'news/(?P<word>.*)/$', views.news, name='news'),
]