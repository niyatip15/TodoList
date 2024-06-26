from django.shortcuts import redirect
from django.urls import reverse_lazy
from base.models import Tasks
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    
class Registeration(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('tasks')
    redirect_authenticated_user = True

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(Registeration,self).form_valid(form)
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(Registeration,self).get(*args, **kwargs)
    
class TaskMixin(LoginRequiredMixin):
    model = Tasks
    context_object_name ="data"
    success_url = reverse_lazy('tasks')

class TasksList(TaskMixin,ListView):
    template_name = 'base/tasks_list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = context['data'].filter(user=self.request.user)
        context['count'] = context['data'].filter(completed=False).count()
        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['data'] = context['data'].filter(title__startswith=search_input)
        context['search_input'] = search_input
        return context

class TaskDetail(TaskMixin,DetailView):
    template_name = 'base/task_detail.html'

class TaskCreate(TaskMixin,CreateView):
    fields = ['title','description','completed']
    template_name = 'base/tasks.html'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(TaskMixin,UpdateView):
    fields = ['title','description','completed']
    template_name = 'base/tasks.html'

class TaskDelete(TaskMixin,DeleteView):
    template_name = 'base/task_delete.html'
