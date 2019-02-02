from django import forms

from .models import Comporisoon

class ComporisoonForm(forms.ModelForm):
    class Meta:
        model = Comporisoon
    fields = []