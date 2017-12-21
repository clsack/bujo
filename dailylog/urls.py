#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:26:50 2017

@author: carolinalissack
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
