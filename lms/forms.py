from django import forms
from .models import *

class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'