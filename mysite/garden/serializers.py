from rest_framework import serializers
from garden.models import SensorReading

class SensorReadingSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(SensorReadingSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = SensorReading
        fields = [
            'id',
            'temp1', 'temp2',
            'rh1', 'rh2',
            'light',
            'timestamp'
        ]

# class SensorReadingSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     temp1 = serializers.FloatField()
#     temp2 = serializers.FloatField()
#     rh1 = serializers.FloatField()
#     rh2 = serializers.FloatField()
#     light = serializers.IntegerField()
#     timestamp = serializers.IntegerField()

#     def create(self, validated_data):
#         """
#         Create and return a new `SensorReading` instance, given the validated data.
#         """
#         return SensorReading.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `SensorReading` instance, given the validated data.
#         """
#         instance.temp1 = validated_data.get('temp1', instance.temp1)
#         instance.temp2 = validated_data.get('temp2', instance.temp2)
#         instance.rh1 = validated_data.get('rh1', instance.rh1)
#         instance.rh2 = validated_data.get('rh2', instance.rh2)
#         instance.light = validated_data.get('light', instance.light)
#         instance.timestamp = validated_data.get('timestamp', instance.timestamp)
#         instance.save()
#         return instance