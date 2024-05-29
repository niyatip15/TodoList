from django.shortcuts import render
from django.urls import reverse_lazy
from base.models import Tasks
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class TasksList(LoginRequiredMixin,ListView):
    model = Tasks
    context_object_name = "data"
    template_name = 'base/tasks_list.html'

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Tasks
    context_object_name = 'data'
    template_name = 'base/task_detail.html'

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'base/tasks.html'

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'base/tasks.html'

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Tasks
    template_name = 'base/task_delete.html'
    context_object_name = 'data'
    success_url = reverse_lazy('tasks')
