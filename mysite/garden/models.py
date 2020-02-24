from django.db import models

# Create your models here.
class SensorReading(models.Model):
    temp1 = models.FloatField()
    temp2 = models.FloatField()
    rh1 = models.FloatField()
    rh2 = models.FloatField()
    light = models.IntegerField()
    timestamp = models.BigIntegerField(unique=True)

    