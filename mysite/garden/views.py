import datetime
from django.views.generic import DetailView, ListView, TemplateView
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from rest_framework import generics, viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from garden.models import ProjectConnection, SensorReading
from garden.serializers import SensorReadingSerializer
from blog.models import Post, Project

from django.db.models import Avg, F, RowRange, Window





class SensorReadingViewSet(viewsets.ModelViewSet):    
    serializer_class = SensorReadingSerializer

    def get_queryset(self):
        queryset = SensorReading.objects.all().order_by('timestamp')

        sensor = self.request.query_params.get('sensor', None)
        if sensor is not None:
            queryset = queryset.filter(sensorID=sensor)
        latest = self.request.query_params.get('latest', None)
        if latest is not None:
            most_recent = queryset.last().timestamp
            # print(most_recent)
            queryset = queryset.exclude(timestamp__lt=most_recent)
        hours = self.request.query_params.get('hours', None)
        if hours is not None:
            try:
                last_reading = queryset.last().timestamp
                earliest_reading = int(last_reading - (float(hours) * 3600))
                queryset = queryset.exclude(timestamp__lt=earliest_reading)
                print(last_reading)
            except Exception as e:
                print("[garden.views] we failed in SensorReadingViewSet")
                print(e)
                pass
        return queryset

class SensorReadingList(APIView):
    """
    List all SensorReadings, or create a new SensorReading.
    """
    def get(self, request, format=None):
        sensor_readings = SensorReading.objects.all().order_by('timestamp')
        # print(sensor_readings.count())

        items = SensorReading.objects.all().order_by('timestamp')[::2]
        # print(items)
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

class Garden(TemplateView):
    template_name='garden/garden.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Get last sensor reading
        last_reading = SensorReading.objects.all().last()
        last_reading_list = {
            "environment":{
                "name": "Environment",
                "light":last_reading.light,
                "temp":round(last_reading.temp1 * 1.8 + 32, 1),
                "rh":round(last_reading.rh1, 1),
                "timestamp":datetime.datetime.fromtimestamp(last_reading.timestamp)
            },
            "greenhouse":{
                "name": "Greenhouse",
                "light":last_reading.light,
                "temp":round(last_reading.temp2 * 1.8 + 32, 1),
                "rh":round(last_reading.rh2, 1),
                "timestamp":datetime.datetime.fromtimestamp(last_reading.timestamp)
            }
        }
        context['current_conditions'] = last_reading_list
        return context

class PostListView(ListView):
    template_name = 'garden/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.exclude(published_date__isnull=True).order_by('-published_date')
    model = Post
    # print(queryset)

class PostDetailView(DetailView):
    model = Post
    template_name = 'garden/post_detail_view.html'
    context_object_name = 'post'

def AboutView(request):
    arduino_pk = ProjectConnection.objects.all().first()
    if arduino_pk:
        project = get_object_or_404(Project, pk=arduino_pk.project.pk)    
        posts = project.post.exclude(published_date__isnull=True).order_by('-published_date')
    else:
        raise Http404()
    # print(posts)
    return render(request, 'garden/project_detail.html', {'project':project, 'posts':posts})
# class AboutView(DetailView):
#     arduino_pk = ProjectConnection.objects.all().first()
#     print(arduino_pk)
#     template_name = 'blog/project_detail.html'


#     project = get_object_or_404(Project, pk=pk)    
#     posts = project.post.exclude(published_date__isnull=True).order_by('-published_date')
#     print(posts)
#     return render(request, 'blog/project_detail.html', {'project':project, 'posts':posts})