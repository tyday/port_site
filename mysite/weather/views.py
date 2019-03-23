from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import ListView

from .forms import ObservationForm
from .models import Observation

class ObservationList(ListView):
    model = Observation

# Create your views here.

def weather(request):
    # return HttpResponse("Hello, welcome to the weather app.")
    observations = Observation.objects.order_by('-observation_date')
    # print(observations)
    return render(request, 'weather/weather.html', {'observations':observations})

def observations(request):
    pass

def observation_detail(request):
    pass

@login_required(login_url='/accounts/login/')
def observation_new(request):
    if request.method == 'POST':
        form = ObservationForm(request.POST)
        print('post-- observation_new')
        if form.is_valid():
            print('is valid')
            observation = form.save(commit=False)
            observation.save()
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