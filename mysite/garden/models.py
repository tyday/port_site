from django.db import models
from blog.models import Project

class ProjectConnection(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)

# Create your models here.
class SensorReading(models.Model):
    temp1 = models.FloatField()
    temp2 = models.FloatField()
    rh1 = models.FloatField()
    rh2 = models.FloatField()
    light = models.IntegerField()
    timestamp = models.BigIntegerField(unique=True)

    