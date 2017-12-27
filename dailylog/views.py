from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views import generic
from django.urls import reverse_lazy
from .models import Event, Appointment, Task, Deadline, Expense, Note
# Create your views here.


def index(request):
    return render(request, 'index.html')


class EventCreate(CreateView):
    model = Event
    fields = ['event_text', 'date_from', 'date_to']
    template_name = 'events/form.html'


class EventUpdate(UpdateView):
    model = Event
    fields = ['event_text', 'date_from', 'date_to']
    template_name = 'events/form.html'


class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('index')
    template_name = 'events/confirm_delete.html'


class EventDetail(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'


class EventListView(ListView):
    model = Event
    template_name = 'events/list.html'


class AppointmentCreate(CreateView):
    model = Appointment
    fields = ['appointment_text', 'date_from', 'date_to', 'location']
    template_name = 'appointments/form.html'


class AppointmentUpdate(UpdateView):
    model = Appointment
    fields = ['appointment_text', 'date_from', 'date_to', 'location']
    template_name = 'appointments/form.html'


class AppointmentDelete(DeleteView):
    model = Appointment
    success_url = reverse_lazy('index')
    template_name = 'appointments/confirm_delete.html'


class AppointmentDetail(generic.DetailView):
    model = Appointment
    template_name = 'appointments/detail.html'


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointments/list.html'


class TaskCreate(CreateView):
    model = Task
    fields = ['task_text', 'date_scheduled', 'date_completed', 'completed']
    template_name = 'tasks/form.html'


class TaskUpdate(UpdateView):
    model = Task
    fields = ['task_text', 'date_scheduled', 'date_completed', 'completed']
    template_name = 'tasks/form.html'


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('index')
    template_name = 'tasks/confirm_delete.html'


class TaskDetail(generic.DetailView):
    model = Task
    template_name = 'tasks/detail.html'


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/list.html'


class DeadlineCreate(CreateView):
    model = Deadline
    fields = ['deadline_text', 'date_scheduled']
    template_name = 'deadlines/form.html'


class DeadlineUpdate(UpdateView):
    model = Deadline
    fields = ['deadline_text', 'date_scheduled']
    template_name = 'deadlines/form.html'


class DeadlineDelete(DeleteView):
    model = Deadline
    success_url = reverse_lazy('index')
    template_name = 'deadlines/confirm_delete.html'


class DeadlineDetail(generic.DetailView):
    model = Deadline
    template_name = 'deadlines/detail.html'


class DeadlineListView(ListView):
    model = Deadline
    template_name = 'deadlines/list.html'


class ExpenseCreate(CreateView):
    model = Expense
    fields = ['expense_text', 'date_scheduled', 'amount', 'currency', 'paid']
    template_name = 'expenses/form.html'


class ExpenseUpdate(UpdateView):
    model = Expense
    fields = ['expense_text', 'date_scheduled', 'amount', 'currency', 'paid']
    template_name = 'expenses/form.html'


class ExpenseDelete(DeleteView):
    model = Expense
    success_url = reverse_lazy('index')
    template_name = 'expenses/confirm_delete.html'


class ExpenseDetail(generic.DetailView):
    model = Expense
    template_name = 'expenses/detail.html'


class ExpenseListView(ListView):
    model = Expense
    template_name = 'expenses/list.html'


class NoteCreate(CreateView):
    model = Note
    fields = ['note_text']
    template_name = 'notes/form.html'


class NoteUpdate(UpdateView):
    model = Note
    fields = ['note_text']
    template_name = 'notes/form.html'


class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('index')
    template_name = 'notes/confirm_delete.html'


class NoteDetail(generic.DetailView):
    model = Note
    template_name = 'notes/detail.html'


class NoteListView(ListView):
    model = Note
    template_name = 'notes/list.html'
