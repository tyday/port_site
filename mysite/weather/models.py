from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

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
    CLOUD_COVERAGE_CHOICES = (('Full coverage', 'Full coverage, little or no sky'), 
                            ('Heavy coverage','Heavy coverage, small patches of sky'),
                            ('Medium coverage','Medium coverage, about half clouds and half sky'),
                            ('Light coverage', 'Light coverage, very few clouds'),
                            ('None','No clouds')                            
                            )
    cloud_coverage = models.CharField(max_length=255, choices=CLOUD_COVERAGE_CHOICES, default='None')

    PRECIPITATION_CHOICES = (
                            ('No precipitation', 'No precipitation'),
                            ('Drizzle', 'Drizzle'),
                            ('Rain','Rain'),
                            ('Hail','Hail'),
                            ('Snow','Snow'),
                            ('Sleet/freezing rain', 'Sleet/freezing rain'),
                            ('Other','Other')
    )
    precipitation_observation = models.CharField(max_length=255, choices=PRECIPITATION_CHOICES, default='No precipitation')
    PHENOM_CHOICES =(
                    ('Nothing','Nothing'),
                    ('Fog/Mist','Fog/Mist'),
                    ('Dew','Dew'),
                    ('Frost','Frost'),
                    ('Rainbow','Rainbow')
    )
    phenomena_observation = models.CharField(max_length=255, choices=PHENOM_CHOICES, default='Nothing')

    def __str__(self):
        return self.observation_date

