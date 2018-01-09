from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views import generic
from django.urls import reverse_lazy
from .models import Habit


def index(request):
    return render(request, 'index.html')


class HabitCreate(CreateView):
    model = Habit
    fields = ['habit_text', 'date_scheduled', 'date_completed', 'completed']
    template_name = 'habits/form.html'


class HabitUpdate(UpdateView):
    model = Habit
    fields = ['habit_text', 'date_scheduled', 'date_completed', 'completed']
    template_name = 'habits/form.html'


class HabitDelete(DeleteView):
    model = Habit
    success_url = reverse_lazy('index')
    template_name = 'habits/confirm_delete.html'


class HabitDetail(generic.DetailView):
    model = Habit
    template_name = 'habits/detail.html'


class HabitListView(ListView):
    model = Habit
    template_name = 'habits/list.html'
