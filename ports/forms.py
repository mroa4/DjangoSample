from django import forms
from django.forms import ModelForm
from ports.models import Port, Trip


class PortForm(ModelForm):
    class Meta:
        model = Port
        fields = ['name', 'temp', 'latitude', 'longitude']

class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['name', 'imo', 'trip_date', 'origin_port','dest_port']
