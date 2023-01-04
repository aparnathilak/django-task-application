from django import forms
from task.models import Tasks
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["task_name"]
        widgets = {
            "task_name": forms.TextInput(attrs={"class":"form-control"})
        }


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model = User
        fields = ["username","email", "password1", "password2"]
        widgets = {
            "email": forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"})
        }
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    