from django import forms
from .models import Observation

class ObservationForm(forms.ModelForm):

    class Meta:
        model = Observation
        fields = ('observer',
                'observation_date',
                'perceived_outdoor_temperature',
                'perceived_outdoor_humidity',
                'observed_outdoor_temperature',
                'observed_outdoor_humidity',
                'observed_outdoor_humidity',
                'observed_pressure_millibars',
                'surface_wind_direction',
                'surface_wind_speed',
                'aloft_wind_direction',
                'aloft_wind_speed',
                'cloud_observation',
                'cloud_coverage',
                'precipitation_observation',
                'phenomena_observation',
                )