from django.shortcuts import render
from django.urls import reverse_lazy
from base.models import Tasks
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class TasksList(ListView):
    model = Tasks
    context_object_name = "data"
    template_name = 'base/tasks_list.html'

class TaskDetail(DetailView):
    model = Tasks
    context_object_name = 'data'
    template_name = 'base/task_detail.html'

class TaskCreate(CreateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('')
    template_name = 'base/tasks.html'

class TaskUpdate(UpdateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('')
    template_name = 'base/tasks.html'

class TaskDelete(DeleteView):
    model = Tasks
    template_name = 'base/task_delete.html'
    context_object_name = 'data'
    success_url = reverse_lazy('view-tasks')

