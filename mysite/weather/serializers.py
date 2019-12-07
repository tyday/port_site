from weather.models import Observation
from rest_framework import serializers

class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = [
             'observer','observation_date', 'perceived_outdoor_temperature', 'perceived_outdoor_humidity'
            ]