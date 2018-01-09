from django.contrib import admin
from .models import Habit
from datetime import datetime
# Register your models here.


def mark_as_completed(modeladmin, request, queryset):
    queryset.update(completed=True, date_completed=datetime.now())


mark_as_completed.short_description = "Mark selected objects as completed"


class HabitAdmin(admin.ModelAdmin):
    list_display = ['habit_text', 'date_scheduled', 'date_completed', 'completed']
    ordering = ['date_scheduled']
    actions = [mark_as_completed]


admin.site.register(Habit, HabitAdmin)
