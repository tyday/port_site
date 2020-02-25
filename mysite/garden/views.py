from django.views.generic import TemplateView
from rest_framework import generics, viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from garden.models import SensorReading
from garden.serializers import SensorReadingSerializer

from django.db.models import Avg, F, RowRange, Window

# class SensorReadingList(generics.ListCreateAPIView):
#     queryset = SensorReading.objects.all()
#     serializer_class = SensorReadingSerializer
class SensorReadingViewSet(viewsets.ModelViewSet):
    queryset = SensorReading.objects.all().order_by('timestamp')
    serializer_class = SensorReadingSerializer

class SensorReadingList(APIView):
    """
    List all SensorReadings, or create a new SensorReading.
    """
    def get(self, request, format=None):
        sensor_readings = SensorReading.objects.all().order_by('timestamp')
        print(sensor_readings.count())
        # items = sensor_readings.annotate(
        #     avg=Window(
        #         expression=Avg('temp1'), 
        #         order_by=F('timestamp').asc(), 
        #         frame=RowRange(start=-2,end=0)
        #     )
        
        # )
        items = SensorReading.objects.all().order_by('timestamp')[::2]
        print(items)
        serializer = SensorReadingSerializer(sensor_readings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SensorReadingSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SensorReadingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingSerializer

class Plots(TemplateView):
    template_name='garden/plots.html'