from django import forms
from .models import Movies

class Moviefrom(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['name','year','disc','img']