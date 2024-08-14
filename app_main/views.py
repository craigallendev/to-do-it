from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView, FormView)
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
    # Takes authenticated users to a different page
    redirect_authenticated_user = True

    def get_success_url(self):
        # Redirects authenticated users to the
        # 'tasks' page after successful login
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    # Registration page for new users
    template_name = 'app_main/register.html'
    form_class = UserCreationForm  # Built-in user creation form
    # Takes authenticated users to a different page
    redirect_authenticated_user = True
    # URL to redirect after successful registration
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        # Handles user registration and logs in the user
        user = form.save()
        if user is not None:
            # Log the user in after successful registration
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *view_args, **view_kwargs):
        # Takes to the 'tasks' page if the user is already authenticated
        if self.request.user.is_authenticated:
            return render(self.request, 'app_main/tasks.html')
        return super(RegisterPage, self).get(*view_args, **view_kwargs)


class TaskList(LoginRequiredMixin, ListView):
    # View to list tasks for a logged-in user
    model = Task
    # The name of the context variable to use in the template
    context_object_name = 'tasks'

    def get_context_data(self, **context_kwargs):
        # Add additional context to the template
        context = super().get_context_data(**context_kwargs)
        context['tasks'] = context['tasks'].filter(
            user=self.request.user)  # Filter tasks by the current user
        context['count'] = context['tasks'].filter(
            complete=False).count()  # Count of incomplete tasks
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__startswith=search_input)
            # Filter tasks based on the search input

        # Add a search input to context for the template
        context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    # View to show details of a specific task
    model = Task
    # The name of the context variable to use in the template
    context_object_name = 'task'
    # Template to use to render the task details
    template_name = 'app_main/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # Fields to be used in the form
    fields = 'title', 'description', 'complete', 'category', 'priority'
    # URL to redirect after successful task creation
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        # Set the current user as the owner of the task
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    # View to update an existing task
    model = Task
    # Fields to be used in the form
    fields = 'title', 'description', 'complete', 'category', 'priority'
    # URL to redirect after successful task update
    success_url = reverse_lazy('tasks')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    # The name of the context variable to use in the template
    context_object_name = 'task'
    # URL to redirect after successful task deletion
    success_url = reverse_lazy('tasks')
    # Template to use for confirming task deletion
    template_name = 'app_main/task_delete.html'


class ToggleTaskCompleteView(View):
    # View to toggle the completion status of a task
    def post(self, request, pk, *args, **kwargs):
        # Get the task object or return a 404 error if not found
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.complete = not task.complete  # Toggle the completion status
        task.save()  # Save the updated task status
        return redirect('tasks')  # Redirect to the 'tasks' page after updating
