from django import forms
from .models import *

class imageform(forms.ModelForm):
    class Meta:
        model = image
        fields = "__all__"
        labels = {"photo":""}
    