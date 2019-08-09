import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as pyo
from pytz import timezone
from django.utils.timezone import localtime

from weather.models import Observation

def temperature_difference(a,b):
    if not a:
        return 0
    if not b:
        return 0
    return a-b


def weather_plot():

    # dates = [a.observation_date.date() for a in Observation.objects.all()]
    dates = [a.observation_date.replace(
        minute=0, second=0) for a in Observation.objects.all().order_by('observation_date')]
    observed_temps = [
        a.observed_outdoor_temperature for a in Observation.objects.all().order_by('observation_date')]
    perceived_temps = [
        a.perceived_outdoor_temperature for a in Observation.objects.all().order_by('observation_date')]
    # temp_difference = [
    #     a.perceived_outdoor_temperature - a.observed_outdoor_temperature for a in Observation.objects.all()
    # ]
    temp_difference = [diff for diff in map(temperature_difference, perceived_temps,observed_temps)]
    # print(temp_difference)
    # fig = make_subplots(specs=[[{"secondary_y": True}]])
    trace0 = go.Scatter(
        x=dates,
        y=observed_temps,
        mode='lines+markers',
        name='Observed Temperature',
        text=[a for a in temp_difference],
        marker = {
            'size':[abs(a) for a in temp_difference],
            'sizemode':'area',
            'sizeref':2.*float(max(temp_difference))/(20.**2),
            'sizemin':0,
            'color': temp_difference,
            'colorscale':'Bluered',
            'showscale':True,
            'colorbar': {
                'title':{'text':'Difference between perceived and observed','side':'right'},
            },            
            # 'title':'Difference between perceived and observed'
        },
        line={
            'shape':'spline',
            'smoothing':.5
        }
        )
    layout = go.Layout(
        title='Perceived and observed temperarture',
        xaxis= {
            'title':'Date'
        },
        yaxis={
            'title':'Fahrenheit'
        },
        # height=800,
    )

    fig = go.Figure(data=[trace0],layout=layout)
    plot = pyo.plot(fig, include_plotlyjs=False, output_type='div')
    return plot

def time_of_readings():
    eastern = timezone('US/Eastern')
    # dates = [a.observation_date.astimezone(eastern).strftime('%I %p') for a in Observation.objects.all()]
    # dates = [a.observation_date.astimezone(eastern).strftime('%I %p') for a in Observation.objects.order_by('observation_date__hour')]
    dates = [a.observation_date.astimezone(eastern) for a in Observation.objects.order_by('observation_date__hour')]
    dates = sorted(dates, key=lambda time: time.hour)
    dates = [date.strftime('%I %p') for date in dates]
    print(dates)
    date_dict = {}
    for date in dates:
        if date in date_dict:
            date_dict[date] += 1
        else:
            date_dict[date] = 1
    data = [
        go.Bar(
            x=list(date_dict.keys()),
            y=list(date_dict.values())
        )
    ]
    layout = go.Layout(
        title='Distribution of observations by time of day',
        xaxis={
            'title':'Hour of day'
        },
        yaxis={
            'title':'Number of observations'
        }
    )
    fig = go.Figure(data=data,layout=layout)
    plot = pyo.plot(fig, include_plotlyjs=False, output_type='div')
    return plot

if __name__ == '__main__':
    # weather_plot()
    time_of_readings()
