# from django import forms
# from .models import Task

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['description', 'due_date', 'initiation_days']
#         widgets = {
#             'due_date': forms.DateInput(attrs={'type': 'date'}),
#             'initiation_days': forms.NumberInput(attrs={'min': 0}),
#         }

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'due_date', 'initiation_time', 'completed']
