from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Cloud_coverage_choices(models.Model):
    cloud_coverage_short = models.CharField(max_length=255)
    cloud_coverage_long = models.CharField(max_length=255)
    def __str__(self):
        return self.cloud_coverage_long
        
class Precipitation_choices(models.Model):
    precipitation_type = models.CharField(max_length=255)
    def __str__(self):
        return self.precipitation_type
class Phenomena_choice(models.Model):
    phenomena = models.CharField(max_length=255)
    def __str__(self):
        return self.phenomena

class Observation(models.Model):
    observer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    observation_date = models.DateTimeField(default=timezone.now)
    perceived_outdoor_temperature = models.DecimalField(max_digits=4,decimal_places=1)
    perceived_outdoor_humidity = models.IntegerField()
    observed_outdoor_temperature = models.DecimalField(max_digits=4,decimal_places=1,blank=True, null=True)
    observed_outdoor_humidity = models.IntegerField(blank=True, null=True)
    observed_pressure_millibars = models.IntegerField(blank=True, null=True)
    

    surface_wind_direction =  models.IntegerField()
    surface_wind_speed = models.IntegerField()
    aloft_wind_direction =  models.IntegerField(blank=True, null=True)
    aloft_wind_speed = models.IntegerField(blank=True, null=True)

    cloud_observation = models.CharField(max_length=255)
    cloud_coverage = models.ForeignKey(Cloud_coverage_choices,on_delete=models.CASCADE, blank=True,null=True)
    
    precipitation_observation = models.ForeignKey(Precipitation_choices,on_delete=models.CASCADE, blank=True, null=True)
    phenomena_observation = models.ForeignKey(Phenomena_choice,on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return str(self.observation_date)

