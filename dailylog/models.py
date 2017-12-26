from django.db import models

# Create your models here.


class Event(models.Model):
    event_text = models.CharField(max_length=100, verbose_name='Description')
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()

    def __str__(self):
        return self.event_text

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('event-detail', kwargs={'pk': self.pk})


class Appointment(models.Model):
    appointment_text = models.CharField(max_length=100, verbose_name='Description')
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.appointment_text

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('appointment-detail', kwargs={'pk': self.pk})


class Task(models.Model):
    task_text = models.CharField(max_length=100, verbose_name='Description')
    date_scheduled = models.DateField()
    date_completed = models.DateField()
    completed = models.BooleanField()

    def __str__(self):
        return self.task_text

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('task-detail', kwargs={'pk': self.pk})


class Deadline(models.Model):
    deadline_text = models.CharField(max_length=100, verbose_name='Description')
    date_scheduled = models.DateTimeField()

    def __str__(self):
        return self.deadline_text

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('deadline-detail', kwargs={'pk': self.pk})


class Expense(models.Model):
    ARS = 'ARS'
    BRL = 'BRL'
    USD = 'USD'
    UYU = 'UYU'
    CURRENCY = (
        (ARS, 'Argentina Peso'),
        (BRL, 'Brazil Real'),
        (USD, 'United States Dollar'),
        (UYU, 'Uruguay Peso')
    )
    expense_text = models.CharField(max_length=255, verbose_name='Description')
    date_scheduled = models.DateField()
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY, default=ARS)
    paid = models.BooleanField()

    def __str__(self):
        return self.expense_text

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('expense-detail', kwargs={'pk': self.pk})


class Note(models.Model):
    note_text = models.CharField(max_length=500, verbose_name='Description')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.note_text

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('note-detail', kwargs={'pk': self.pk})
