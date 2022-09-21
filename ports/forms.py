from django import forms
from django.forms import ModelForm
from ports.models import Port


class PortForm(ModelForm):
    class Meta:
        model = Port
        fields = ['name', 'temp', 'latitude', 'longitude']
