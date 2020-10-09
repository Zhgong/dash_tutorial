import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='Montréal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])


@app.callback(Output('output-state', 'children'), [
    Input('submit-state', 'n_clicks'),
    State('input-1-state', 'value'),
    State('input-2-state', 'value'),
])
def update_value(n_clicks, input1, input2):
    return f'''
    The Button has been clicked {n_clicks} times.
    input1 is '{input1}'
    input2 is '{input2}'
    '''


if __name__ == '__main__':
    app.run_server(debug=True)