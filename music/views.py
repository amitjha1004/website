# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Album


def index(request):
#    all_albums = Album.objects.all()
 #   template = loader.get_template('')
  #  return HttpResponse('')
  #   numbers = [1,2,3,4,5]
  #   name = 'AMIT JHA'

  # args = {'myName' : name}
  return render (request,'music/login.html') #,args)


def detail(request, album_id):
    return HttpResponse


