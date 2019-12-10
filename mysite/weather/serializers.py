from weather.models import Observation
from rest_framework import serializers

class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = [
             'observer',
             'observation_date',
             'perceived_outdoor_temperature',
             'perceived_outdoor_humidity',
             'observed_outdoor_temperature',
             'observed_outdoor_humidity',
             'observed_pressure_millibars',
             'surface_wind_direction',
             'surface_wind_speed',
             'cloud_observation',
             'cloud_coverage',
            ]