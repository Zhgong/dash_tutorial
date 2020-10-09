import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}
app.layout = html.Div([
    dcc.RadioItems(id='countries-radio',
                   options=[{
                       'label': k,
                       'value': k
                   } for k in all_options.keys()],
                   value='America'),
    html.Hr(),
    dcc.RadioItems(id='cities-radio'),
    html.Hr(),
    html.Div(id='display-selected-values')
])


@app.callback(Output('cities-radio', 'options'),
              Input('countries-radio', 'value'))
def update_coutries(country):
    return [{'label': k, 'value': k} for k in all_options.get(country)]


@app.callback(Output('cities-radio', 'value'),
              Input('cities-radio', 'options'))
def update_cities_option(options):
    return options[0]['value']

@app.callback(Output('display-selected-values', 'children'),
              [Input('cities-radio', 'value'),Input('countries-radio', 'value')
              ])
def update_dislpay(city, country):
    return f'{city} is in {country}'





if __name__ == '__main__':
    app.run_server(debug=True)