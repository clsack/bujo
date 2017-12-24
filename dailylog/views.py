from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from .models import Event, Appointment, Task, Deadline, Expense, Note
# Create your views here.


def index(request):
    return HttpResponse("Daily log")


class EventCreate(CreateView):
    model = Event
    fields = ['event_text', 'date_from', 'date_to']


class EventUpdate(UpdateView):
    model = Event
    fields = ['event_text', 'date_from', 'date_to']


class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('index')


class EventDetail(generic.DetailView):
    model = Event


class AppointmentCreate(CreateView):
    model = Appointment
    fields = ['appointment_text', 'date_from', 'date_to', 'location']


class AppointmentUpdate(UpdateView):
    model = Appointment
    fields = ['appointment_text', 'date_from', 'date_to', 'location']


class AppointmentDelete(DeleteView):
    model = Appointment
    success_url = reverse_lazy('index')


class AppointmentDetail(generic.DetailView):
    model = Appointment


class TaskCreate(CreateView):
    model = Task
    fields = ['task_text', 'date_scheduled', 'date_completed', 'completed']


class TaskUpdate(UpdateView):
    model = Task
    fields = ['task_text', 'date_scheduled', 'date_completed', 'completed']


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('index')


class TaskDetail(generic.DetailView):
    model = Task


class DeadlineCreate(CreateView):
    model = Deadline
    fields = ['deadline_text', 'date_scheduled']


class DeadlineUpdate(UpdateView):
    model = Deadline
    fields = ['deadline_text', 'date_scheduled']


class DeadlineDelete(DeleteView):
    model = Deadline
    success_url = reverse_lazy('index')


class DeadlineDetail(generic.DetailView):
    model = Deadline


class ExpenseCreate(CreateView):
    model = Expense
    fields = ['expense_text', 'date_scheduled', 'amount', 'currency', 'paid']


class ExpenseUpdate(UpdateView):
    model = Expense
    fields = ['expense_text', 'date_scheduled', 'amount', 'currency', 'paid']


class ExpenseDelete(DeleteView):
    model = Expense
    success_url = reverse_lazy('index')


class ExpenseDetail(generic.DetailView):
    model = Expense


class NoteCreate(CreateView):
    model = Note
    fields = ['note_text']


class NoteUpdate(UpdateView):
    model = Note
    fields = ['note_text']


class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('index')


class NoteDetail(generic.DetailView):
    model = Note
