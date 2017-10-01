# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class users(models.Model):
    your_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    #company start date is default (my birthday)
    date_hired = models.DateField(blank = False)
    pword=models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return "{} {}".format(self.your_name, self.user_name)

class wishes(models.Model):
    item = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)
    #link wishes to person
    who = models.ForeignKey(users, related_name='wishy')
    fans = models.ManyToManyField(users, related_name="favorite")

    def __str__(self):
        return self.item

class favorite(models.Model):
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)
    likes = models.ForeignKey(users, related_name='washy', default=False)
    liked = models.ForeignKey(wishes, related_name='wishes', default=False)