import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

df = pd.read_csv('data.csv')


title = 'Overnatning'


overnatningsformer = df.OVERNATF.unique()
omraader = df.OMRÅDE.unique()
nationer = df.NATION1.unique()



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Woco Dashboard'),

    html.Div(children='''
       v. 0.01.
    '''),


    html.Label('Vælg overnatningsform'),
    dcc.Dropdown(
        id='vaelg-overnatningsform',
        options=[{'label': i, 'value': i} for i in overnatningsformer],
        value='Hoteller og Feriecentre i alt'
    ),


    html.Label('Vælg område'),
    dcc.Dropdown(
        id='vaelg-omraade',
        options=[{'label': i, 'value': i} for i in omraader],
        value='Landsdel København By'
    ),

    html.Label('Vælg nation'),
    dcc.Dropdown(
        id = 'vaelg-nation',
        options=[{'label': i, 'value': i} for i in nationer],
        value='I alt'
    ),

    html.Table(id='my_table'),
    dcc.Graph(id='overnatninger')
])

@app.callback(
    Output('overnatninger', 'figure'),
    [Input('vaelg-overnatningsform', 'value'),
     Input('vaelg-omraade', 'value'),
     Input('vaelg-nation', 'value'),
    ])
def update_figure(overnatningsform, omraade, nation):
    #omraade = 'Landsdel København By'
    #nation = 'I alt'

    sub_df = df[(df.OVERNATF == overnatningsform)&(df.OMRÅDE == omraade)&(df.NATION1 == nation)]
    trace1 = go.Scatter(
            x = sub_df.Timestamp,
            y = sub_df.INDHOLD,
            mode='lines',
            name = overnatningsform + ' ' + omraade + ' ' + nation,
            #connectgaps=True,
    )

    traces = [trace1]

    return(
        {
        'data': traces 
        }


        )


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


@app.callback(Output('my_table', 'children'), [Input('vaelg-overnatningsform', 'value')])
def update_table(value):
    sub_df = df[(df.OVERNATF == value)]
    table = generate_table(sub_df) 
    return table

if __name__ == '__main__':
    app.run_server(debug=True)