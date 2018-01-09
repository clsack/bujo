from django.db import models
from django.urls import reverse


class Habit(models.Model):
    habit_text = models.CharField(max_length=100, verbose_name='Description')
    date_scheduled = models.DateField()
    date_completed = models.DateField(null=True, blank=True)
    completed = models.BooleanField()

    class Meta:
        ordering = ['date_scheduled']
        get_latest_by = ['-date_scheduled']

    def __str__(self):
        return self.habit_text

    def get_absolute_url(self):
        return reverse('habit-detail', kwargs={'pk': self.pk})
