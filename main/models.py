from django.db import models

# Create your models here.


class Appearence(models.Model):
    obj_name = models.CharField(default='', max_length=100)
    title = models.CharField(max_length=100)
    desc = models.TextField(default='.')  # decsription,
    facebook = models.CharField(default='https://facebook.com', max_length=100) 
    twitter = models.CharField(default='https://youtube.com', max_length=100) 
    youtube = models.CharField(default='https://twitter.com', max_length=100)
    footer_credit = models.TextField(default='Copyright ©2021 All rights reserved | Developed  by Django Team', max_length=160)
    mobile = models.CharField(default='+8801234567890', max_length=100)

    def __str__(self):
        return self.obj_name.strip()
