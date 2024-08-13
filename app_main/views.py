from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task

class CustomLoginView(LoginView):
    # Custom login view to specify the template and handle redirection
    template_name = 'app_main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True # Takes authenticated users to a different page

    def get_success_url(self):
        # Redirects authenticated users to the 'tasks' page after successful login
        return reverse_lazy('tasks')

class RegisterPage(FormView):
    # Registration page for new users
    template_name = 'app_main/register.html'
    form_class = UserCreationForm # Built-in user creation form
    redirect_authenticated_user = True # Takes authenticated users to a different page
    success_url = reverse_lazy('tasks') # URL to redirect after successful registration

    def form_valid(self, form):
        # Handles user registration and logs in the user
        user = form.save()
        if user is not None:
            login(self.request, user) # Log the user in after successful registration
        return super(RegisterPage, self).form_valid(form)

    def get(self, *view_args, **view_kwargs):
        # Takes to the 'tasks' page if the user is already authenticated
        if self.request.user.is_authenticated:
            return render(self.request, 'app_main/tasks.html')
        return super(RegisterPage, self).get(*view_args, **view_kwargs)
class TaskList(LoginRequiredMixin, ListView):
    # View to list tasks for a logged-in user
    model = Task
    context_object_name = 'tasks' # The name of the context variable to use in the template

    def get_context_data(self, **context_kwargs):
        # Add additional context to the template
        context = super().get_context_data(**context_kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user) # Filter tasks by the current user
        context['count'] = context['tasks'].filter(complete=False).count() # Count of incomplete tasks
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter( 
                title__startswith=search_input) # Filter tasks based on the search input

        context['search_input'] = search_input # Add a search input to context for the template
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    # View to show details of a specific task
    model = Task
    context_object_name = 'task' # The name of the context variable to use in the template
    template_name = 'app_main/task.html' # Template to use to render the task details

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = 'title', 'description', 'complete', 'category', 'priority' # Fields to be used in the form
    success_url = reverse_lazy('tasks') # URL to redirect after successful task creation

    def form_valid(self, form):
        # Set the current user as the owner of the task
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    # View to update an existing task
    model = Task
    fields = 'title', 'description', 'complete', 'category', 'priority' # Fields to be used in the form
    success_url = reverse_lazy('tasks') # URL to redirect after successful task update

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task' # The name of the context variable to use in the template
    success_url = reverse_lazy('tasks') # URL to redirect after successful task deletion
    template_name = 'app_main/task_delete.html' # Template to use for confirming task deletion

class ToggleTaskCompleteView(View):
     # View to toggle the completion status of a task
    def post(self, request, pk, *args, **kwargs):
        # Get the task object or return a 404 error if not found
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.complete = not task.complete # Toggle the completion status
        task.save() # Save the updated task status
        return redirect('tasks')  # Redirect to the 'tasks' page after updating