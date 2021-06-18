from django import forms
from .models import ExcerciseDate, ExcerciseDetail

class ExerciseForm(forms.ModelForm):
    class Meta:
        model=ExcerciseDetail
        fields='__all__'