from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from .forms import ObservationForm

# Create your views here.

def weather(request):
    # return HttpResponse("Hello, welcome to the weather app.")
    return render(request, 'weather/weather.html')

def observation_detail(request):
    pass

def observation_new(request):
    form = ObservationForm(
        initial={
            'observer' : request.user
        }
    )
    return render(request, 'weather/observation_edit.html', {'form': form})