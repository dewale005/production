from django import forms
from django.forms import ModelForm, Textarea

from .models import Employee

class EmployeeForm(forms.ModelForm):
    First_Name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control inlined", "placeholder":"What is your first name?"}))
    Last_Name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"What is your last name?"}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"What is your email address?"}))
    Phone_Number = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"What is your phone number?"}))
    Address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"What is your home address?"}))
    class Meta:
        model = Employee
        fields = '__all__'