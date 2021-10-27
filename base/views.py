
from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from . models import Task
from django.urls import reverse_lazy # redirect after post 

# Create your views here.
class TaskList(ListView):
    model=Task
    context_object_name='tasks'

class TaskDetail(DetailView):
    model=Task
    context_object_name='task'
    template_name='base/task.html'
class TaskCreate(CreateView): #post
    model=Task
    fields='__all__'
    success_url=reverse_lazy('tasks') #redirect
class TaskUpdate(UpdateView):#post
    model=Task
    fields='__all__'
    success_url=reverse_lazy('tasks') #redirect

class TaskDelete(DeleteView):#post
    model=Task
    context_object_name='task'
    success_url=reverse_lazy('tasks') #redirect