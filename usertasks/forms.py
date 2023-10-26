from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Task, User


class TaskForm(forms.ModelForm):
    executor = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ('title', 'description', 'executor', 'completion_date')



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')