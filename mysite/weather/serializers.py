from django.contrib.auth.models import User
from weather.models import Observation, Cloud_coverage_choices
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name']
class CloudCoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloud_coverage_choices
        fields = ['cloud_coverage_short', 'cloud_coverage_long']
class ObservationSerializer(serializers.ModelSerializer):
    observer = UserSerializer(read_only=True)
    cloud_coverage = CloudCoverageSerializer(required=False)
    # observer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Observation
        # depth = 2
        fields = [
            'pk',
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
        read_only_fields = [
            'pk',
        ]