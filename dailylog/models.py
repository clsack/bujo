from django.db import models
from time import date
# Create your models here.


class Event(models.Model):
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    location = models.CharField(max_length=255)


class Appointment(models.Model):
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    location = models.CharField(max_length=255)


class Task(models.Model):
    date_scheduled = models.DateField()
    date_completed = models.DateField()
    completed = models.BooleanField()


class Deadline(models.Model):
    date_scheduled = models.DateTimeField()


class Expense(models.Model):
    ARS = 'ARS'
    BRL = 'BRL'
    USD = 'USD'
    UYU = 'UYU'
    CURRENCY_CHOICES = (
        (ARS, 'Argentina Peso'),
        (BRL, 'Brazil Real'),
        (USD, 'United States Dollar'),
        (UYU, 'Uruguay Peso')
    )
    date_scheduled = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(decimal_places=2)
    currency = models.CharField(max_length=2, choices=CURRENCY_CHOICES, default=ARS)


class Note(models.Model):
    date_scheduled = models.DateField(auto_now_add=True, default=date.today)
    description = models.CharField(max_length=500)
