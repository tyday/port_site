import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as pyo

from models import Observation
fig = make_subplots(specs=[[{"secondary_y":True}]])

trace0 = go.Scatter(
        x=[0, 1, 2, 3, 4, 5],
        y=[12.5, 19, 27.3, 5.7, 1.8, 15.9],
        name='Bar'
    )

trace1 = go.Bar(
        x=[0, 1, 2, 3, 4, 5],
        y=[1, 0.5, 0.7, -1.2, 0.3, 0.4],
        name='Line'
    )


fig.add_trace(trace0,secondary_y=False)
fig.add_trace(trace1,secondary_y=True)

# layout = go.Layout(
#     title="Graph title",
#     yaxis={
#         side:'left',
#         title:'Wind in mph'
#     }
# )
fig.update_layout(
    title_text="Double Y Axis example"
)
fig.update_xaxes(title_text="xaxix title")
fig.update_yaxes(title_text="<b>primary</b> yaxis title", secondary_y=False)
fig.update_yaxes(title_text="<b>secondary</b> yaxis title", secondary_y=True)

# fig = go.Figure(data=[trace0,trace1], layout=layout)
# pyo.plot(fig)
fig.show()