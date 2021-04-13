from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.views.generic import ListView

from rest_framework import viewsets

from .forms import ObservationForm
from .models import Observation
from .plots.observations import weather_plot, time_of_readings
from .serializers import ObservationSerializer
from common.utilities.city_finder import find_city

class ObservationList(ListView):
    model = Observation

# Create your views here.

def weather(request):
    observation_list = Observation.objects.order_by('-observation_date')
    page = request.GET.get('page', 1)

    paginator = Paginator(observation_list, 10)
    try:
        observations = paginator.page(page)
    except PageNotAnInteger:
        observations = paginator.page(1)
    except EmptyPage:
        observations = paginator.page(paginator.num_pages)

    return render(request, 'weather/weather.html', {'observations':observations})

@login_required(login_url='/admin/login/')
def observation_edit(request,pk):
    observation = get_object_or_404(Observation, pk=pk)

    if request.method == 'POST':
        form = ObservationForm(request.POST, request.FILES, instance=observation)
        if form.is_valid():
            observation = form.save(commit=False)
            observation.save()
            return redirect('observation_detail', pk=observation.pk)
        else:
            return render(request, 'weather/observation_edit.html', {'form':form})
    else:
        form = ObservationForm(instance=observation)
        return render(request, 'weather/observation_edit.html', {'form':form})

def observation_detail(request, pk):
    observation = get_object_or_404(Observation, pk=pk)
    return render(request, 'weather/observation_detail.html', {'observation':observation})

@login_required(login_url='/admin/login/')
def observation_new(request):
    if request.method == 'POST':
        form = ObservationForm(request.POST, request.FILES)
        if form.is_valid():
            observation = form.save(commit=False)
            observation.save()
            messages.add_message(request, messages.SUCCESS, 'Your observation was saved.')
            return redirect('weather')
        else:
            print('not valid')
            # form = ObservationForm()
    else:
        form = ObservationForm(
            initial={
                'observer' : request.user
            }
        )
    return render(request, 'weather/observation_edit.html', {'form': form})

def plot(request):
    query = request.GET
    if 'plot' in query:
        if query['plot'] == 'time':
            plot = time_of_readings()
        else:
            plot = weather_plot()
    else:
        plot = weather_plot()
    return render(request, 'weather/plot.html', {'plot': plot})

class ObservationViewSet(viewsets.ModelViewSet):
    queryset = Observation.objects.all().order_by('-observation_date')
    serializer_class = ObservationSerializer

def find_city_req(request):
    response = JsonResponse({'status':'no coordinate information found.'})
    if 'lat' and 'lon' in request.GET:
        try:
            lat, lon = request.GET['lat'],request.GET['lon'],
            lat, lon = float(lat), float(lon)
            city = find_city(lat,lon)
            response = JsonResponse({
                'status': 'Success',
                'city':city.city_name,
                'admin_region':city.admin_name,
                'country': city.country_code
                })
        except:
            response = JsonResponse({'status':'could not convert latitude and longitude to float'})
        
    return response
