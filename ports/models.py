from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Port(models.Model):
    name = models.CharField(null=False, blank=False,
                            max_length=50, unique=True)
    temp = models.FloatField(null=False, blank=False, validators=[
                             MinValueValidator(-30), MaxValueValidator(30)])
    latitude = models.FloatField(null=False, blank=False, validators=[
                                 MinValueValidator(-180), MaxValueValidator(180)])
    longitude = models.FloatField(null=False, blank=False, validators=[
                                  MinValueValidator(-90), MaxValueValidator(90)])
    date = models.DateField(auto_now=True)

class Trip(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    imo = models.IntegerField(null=False, blank=False, unique=True)
    trip_date = models.DateField(null=False, blank=False)
    submit_date = models.DateField(auto_now=True)
    origin_port =  models.ForeignKey(Port, on_delete=models.PROTECT, related_name='origin')
    dest_port = models.ForeignKey(Port, on_delete=models.PROTECT , related_name='destination')
