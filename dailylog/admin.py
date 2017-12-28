from django.contrib import admin
from .models import Event, Appointment, Task, Deadline, Expense, Note
from datetime import datetime
# Register your models here.


def mark_as_completed(modeladmin, request, queryset):
    queryset.update(completed=True, date_completed=datetime.now())


mark_as_completed.short_description = "Mark selected payments as paid"


def mark_as_paid(modeladmin, request, queryset):
    queryset.update(paid=True)


mark_as_completed.short_description = "Mark selected objects as completed"


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Appointment, AppointmentAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_text', 'date_scheduled', 'date_completed', 'completed']
    ordering = ['date_scheduled']
    actions = [mark_as_completed]


admin.site.register(Task, TaskAdmin)


class DeadlineAdmin(admin.ModelAdmin):
    pass


admin.site.register(Deadline, DeadlineAdmin)


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['expense_text', 'date_scheduled', 'amount', 'currency', 'paid']
    ordering = ['date_scheduled']
    actions = [mark_as_paid]


admin.site.register(Expense, ExpenseAdmin)


class NoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Note, NoteAdmin)
