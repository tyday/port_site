from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import ListView

from .forms import ObservationForm
from .models import Observation
from .plots.observations import weather_plot, time_of_readings

class ObservationList(ListView):
    model = Observation

# Create your views here.

def weather(request):
    # return HttpResponse("Hello, welcome to the weather app.")
    observations = Observation.objects.order_by('-observation_date')
    return render(request, 'weather/weather.html', {'observations':observations})

@login_required(login_url='/admin/login/')
def observation_edit(request,pk):
    observation = get_object_or_404(Observation, pk=pk)

    if request.method == 'POST':
        form = ObservationForm(request.POST, instance=observation)
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
        form = ObservationForm(request.POST)
        print('post-- observation_new')
        if form.is_valid():
            print('is valid')
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
    # plot = weather_plot()
    plot = time_of_readings()
    # print(plot)
    return render(request, 'weather/plot.html', {'plot': plot})