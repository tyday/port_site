from django.db import models
from blog.models import Project
import datetime

class ProjectConnection(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)

# Create your models here.
class SensorReading(models.Model):
    sensorID = models.CharField(max_length=20, default="default_sensor")
    temp1 = models.FloatField()
    temp2 = models.FloatField()
    rh1 = models.FloatField()
    rh2 = models.FloatField()
    light = models.IntegerField()
    timestamp = models.BigIntegerField(unique=True)

    def save(self, *args, **kwargs):
        # print(f'Self.timestamp: {self.timestamp}, self.timestamp=true: {not self.timestamp} ')
        if not self.timestamp:
            self.timestamp = int(datetime.datetime.now().timestamp())
        super(SensorReading, self).save(*args, **kwargs)

    