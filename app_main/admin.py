from django.contrib import admin
from .models import Task

# Register the Task model with the Django admin site.
# This makes the Task model available in the Django admin interface,
# Which allows for easy management of Task records.
admin.site.register(Task)