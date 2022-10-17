from django import forms
from map.models import *


class InputForm(forms.ModelForm):
    start = forms.CharField(label='start', max_length=100)
    end = forms.CharField(label='end', max_length=100)
    class Meta:
        model = Result
        fields = ("start",)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


