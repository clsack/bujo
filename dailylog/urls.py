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
    path('events/add/', views.EventCreate.as_view(), name='event-add'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='event-update'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='event-delete'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('appointments/add/', views.AppointmentCreate.as_view(), name='appointment-add'),
    path('appointments/<int:pk>/update/', views.AppointmentUpdate.as_view(), name='appointment-update'),
    path('appointments/<int:pk>/delete/', views.AppointmentDelete.as_view(), name='appointment-delete'),
    path('appointments/<int:pk>/', views.AppointmentDetail.as_view(), name='appointment-detail'),
    path('tasks/add/', views.TaskCreate.as_view(), name='task-add'),
    path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='task-delete'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path('deadlines/add/', views.DeadlineCreate.as_view(), name='deadline-add'),
    path('deadlines/<int:pk>/update/', views.DeadlineUpdate.as_view(), name='deadline-update'),
    path('deadlines/<int:pk>/delete/', views.DeadlineDelete.as_view(), name='deadline-delete'),
    path('deadlines/<int:pk>/', views.DeadlineDetail.as_view(), name='deadline-detail'),
    path('expenses/add/', views.ExpenseCreate.as_view(), name='expense-add'),
    path('expenses/<int:pk>/update/', views.ExpenseUpdate.as_view(), name='expense-update'),
    path('expenses/<int:pk>/delete/', views.ExpenseDelete.as_view(), name='expense-delete'),
    path('expenses/<int:pk>/', views.ExpenseDetail.as_view(), name='expense-detail'),
    path('notes/add/', views.NoteCreate.as_view(), name='note-add'),
    path('notes/<int:pk>/update/', views.NoteUpdate.as_view(), name='note-update'),
    path('notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='note-delete'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='note-detail'),
]
