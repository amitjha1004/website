# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class employees(models.Model):

    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    emp_id=models.IntegerField(primary_key=True)
    # emp_id = models.IntegerField(primary_key=True)



    def __str__(self):
        return self.firstname

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = employees.objects.create(firstname=kwargs['instance'])

    post_save.connect(create_profile, sender=User)