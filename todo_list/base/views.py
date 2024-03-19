from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Task
from datetime import datetime


class TaskList( ListView):
    model = Task
    context_object_name = 'tasks'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = Task.objects.filter(complete=False).count()
        return context

class TaskDetail(DetailView):
    model =Task
    context_object_name='task'
    template_name= 'base/task.html'
    
    
class TaskCreate( CreateView):
    model = Task
    fields =  ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_datetime'] = datetime.now()
        return context
    
class TaskUpdate(UpdateView):
    model =Task
    fields =['title', 'description', 'complete']
    success_url=reverse_lazy('tasks')
    

class TaskDelete(DeleteView):
    model = Task
    context_object_name = "task" # bieens truyen vao
    success_url=reverse_lazy('tasks')

    