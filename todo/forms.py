from .models import Todo
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task']

        widgets = {
            'task': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Add a new task"
            }),
        }
        labels = {
            'task': 'Task name',
        }
