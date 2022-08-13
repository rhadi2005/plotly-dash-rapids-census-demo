import numpy as np # linear algebra
import pandas as pd

import dash
from dash import Dash, html, dcc
import plotly.express as px

#import dash_core_components as dcc
#import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_daq as daq
from plotly.colors import sequential
from pyproj import Transformer

from dask import delayed
from distributed import Client
from dask_cuda import LocalCUDACluster

import cudf
import cupy

#print("Werkzeug ", Werkzeug.__version__)

# Disable cupy memory pool so that cupy immediately releases GPU memory
cupy.cuda.set_allocator(None)

# Colors
bgcolor = "#191a1a"  # mapbox dark map land color
text_color = "#cfd8dc"  # Material blue-grey 100
mapbox_land_color = "#343332"


#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


            
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

            
if __name__ == '__main__':

    # Launch dashboard
    app.run_server(
        debug=True, dev_tools_silence_routes_logging=True, host='0.0.0.0')
        
     
