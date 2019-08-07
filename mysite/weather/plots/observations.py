import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as pyo

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
        minute=0, second=0) for a in Observation.objects.all()]
    observed_temps = [
        a.observed_outdoor_temperature for a in Observation.objects.all()]
    perceived_temps = [
        a.perceived_outdoor_temperature for a in Observation.objects.all()]
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
        height=800,
        # zaxis={
        #     'title':'Difference between perceived and observed'
        # }
    )

    # fig.add_trace(trace0)
    # fig.update_layout(title_text="Double Y Axis example",height=800)
    # fig.update_xaxes(title_text="xaxix title")
    # fig.update_yaxes(title_text="<b>primary</b> yaxis title",
    #                  secondary_y=False)
    # fig.update_yaxes(
    #     title_text="<b>secondary</b> yaxis title", secondary_y=True)
    # fig.show()
    # plot = pyo.plot(fig, include_plotlyjs=False, output_type='div')
    fig = go.Figure(data=[trace0],layout=layout)
    plot = pyo.plot(fig, include_plotlyjs=True, output_type='div')
    # plot = 'heelloo'
    # print(plot)
    return plot


if __name__ == '__main__':
    weather_plot()
