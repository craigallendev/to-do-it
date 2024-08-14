from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    # Display these fields in the task list view
    list_display = ('title', 'user', 'complete',
                    'created', 'category', 'priority')

    # Add a filter sidebar to filter by user and completion status
    list_filter = ('user', 'complete', 'category', 'priority')

    # Add a search bar to search by task title and user username
    search_fields = ('title', 'user__username')

    # Enable ordering by user, and then by completion status
    ordering = ('user', 'complete')


# Register the Task model with the Django admin site.
# This makes the Task model available in the Django admin interface,
# Which allows for easy management of Task records.
admin.site.register(Task, TaskAdmin)
