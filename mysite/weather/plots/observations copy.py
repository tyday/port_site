import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as pyo

from weather.models import Observation


def weather_plot():

    # dates = [a.observation_date.date() for a in Observation.objects.all()]
    dates = [a.observation_date.replace(
        minute=0, second=0) for a in Observation.objects.all()]
    observed_temps = [
        a.observed_outdoor_temperature for a in Observation.objects.all()]
    observed_humidity = [
        a.observed_outdoor_humidity for a in Observation.objects.all()]
    observed_pressure = [
        a.observed_pressure_millibars for a in Observation.objects.all()]
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    trace0 = go.Scatter(x=dates,y=observed_temps,name='Observed Temperature')
    
    trace1 = go.Scatter(
        x=dates,
        y=observed_pressure,
        name='Observed Pressure',
        mode='markers'
    )
    fig.add_trace(trace0, secondary_y=False)
    fig.add_trace(trace1, secondary_y=True)
    fig.update_layout(title_text="Double Y Axis example",height=800)
    fig.update_xaxes(title_text="xaxix title")
    fig.update_yaxes(title_text="<b>primary</b> yaxis title",
                     secondary_y=False)
    fig.update_yaxes(
        title_text="<b>secondary</b> yaxis title", secondary_y=True)
    # fig.show()
    # plot = pyo.plot(fig, include_plotlyjs=False, output_type='div')
    plot = pyo.plot(fig, include_plotlyjs=True, output_type='div')
    # plot = 'heelloo'
    # print(plot)
    return plot


if __name__ == '__main__':
    weather_plot()
