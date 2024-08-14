from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    # Title of the task with a maximum length of 200 characters.
    title = models.CharField(max_length=200)
    # Description of the task, which is optional and can be empty.
    description = models.TextField(null=True, blank=True)
    # Boolean field to show whether the task is completed.
    complete = models.BooleanField(default=False)
    # DateTime field that automatically sets
    # the date and time when the task is created.
    created = models.DateTimeField(auto_now_add=True)
    # Category of the task, with predefined choices.
    # 'blank=True' allows this field to be left empty.
    category = models.CharField(max_length=50,
                                choices=[
                                    ('work', 'Work'),
                                    ('personal', 'Personal'),
                                    ('shopping', 'Shopping'),
                                    ('chore', 'Chore'),
                                    ('study', 'Study'),
                                    ('event', 'Event'),
                                    ('fitness', 'Fitness'),
                                    ('daily_routine', 'Daily Routine'),
                                    ('other', 'Other'),
                                ], blank='True')
    # Priority of the task, with predefined choices.
    # 'blank=True' allows this field to be left empty.
    priority = models.CharField(max_length=50,
                                choices=[
                                    ('high', 'High'),
                                    ('medium', 'Medium'),
                                    ('low', 'Low'),
                                ], blank=True)

    def __str__(self):
        # String display of the task, which returns the task title.
        return self.title

    class Meta:
        # Default ordering of tasks by their completion status.
        # In this case, completed tasks will appear after incomplete tasks.
        ordering = ['complete']
