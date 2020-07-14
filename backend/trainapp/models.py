from django.db import models

# Create your models here.


class Schedule(models.Model):
    train = models.CharField(max_length=25, default=None)
    departure_station = models.CharField(max_length=30, default=None)
    arrival_station = models.CharField(max_length=30, default=None)
    departure_time = models.TimeField(default=None)
    arrival_time = models.TimeField(default=None)
    duration = models.CharField(max_length=5, default=None)
