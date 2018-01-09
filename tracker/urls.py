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
    path('habits/add/', views.HabitCreate.as_view(), name='habit-add'),
    path('habits/<int:pk>/update/', views.HabitUpdate.as_view(), name='habit-update'),
    path('habits/<int:pk>/delete/', views.HabitDelete.as_view(), name='habit-delete'),
    path('habits/<int:pk>/', views.HabitDetail.as_view(), name='habit-detail'),
    path('habits/all/', views.HabitListView.as_view(), name='habit-list'),
]
