from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class News(models.Model):
    obj_name = TextField(default='news_object', max_length='100')
    title = TextField(default='News Title')
    short_summary = TextField(default='This is news short summary')
    deatils = TextField(default='News deatils')
    write = TextField(default='write name')
    date = TextField(default='date')

    def __str__(self):
        return self.obj_name
