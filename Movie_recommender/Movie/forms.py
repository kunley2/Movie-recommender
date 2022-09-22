from django import forms
from .models import Movies


class Moviesform(forms.Form):
    movieslist = forms.ModelChoiceField(queryset=Movies.objects.values_list('Movie_Title',flat=True).order_by('Movie_Title'),
                                        label='Movie Title')