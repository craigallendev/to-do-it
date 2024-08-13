from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    # Override the default 'category' field to use a ModelChoiceField.
    # This field allows selecting a category from a list of existing categories.
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)

    class Meta:
        # Specifies the model associated with this form.
        model = Task
        # List of fields to include in the form.
        fields = ['title', 'description', 'complete', 'category']