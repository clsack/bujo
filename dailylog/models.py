from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=ARS)


class Note(models.Model):
    date_scheduled = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=500)
