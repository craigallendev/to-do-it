from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50,
        choices=[
            ('work', 'Work'),
            ('personal', 'Personal'),
            ('shopping', 'Shopping'),
            ('chore', 'Chore'),
            ('study', 'Study'),
            ('event', 'Event'),
            ('fitness', 'Fitness'),
            ('daily routine', 'Daily Routine'),
            ('other', 'Other'),
    ], blank='True')
    priority = models.CharField(max_length=50,
        choices=[
            ('high', 'High'),
            ('medium', 'Medium'),
            ('low', 'Low'),
    ], blank=True)
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
# Create your models here.
