from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Read data
df = pd.read_csv('../data/totals/1994_player_totals.csv')

# Initialize App
app = Dash(__name__)

# Layout

app.layout = html.Div([
    html.Div(children='App with Data, Graph, and Controls'),
    html.Hr(),
    dcc.RadioItems(options=['PTS', 'AST', 'STL', 'BLK','TRB', 'eFG%', 'MP'], value='PTS', id='controls-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=20),
    dcc.Graph(figure={}, id='controls-graph')
])

# Add Controls
@callback(
    Output(component_id='controls-graph', component_property='figure'),
    Input(component_id='controls-radio-item', component_property='value')
)

def update_graph(col_chosen):
    fig = px.histogram(df, x='Pos', y=col_chosen, histfunc='avg')
    return fig
    
    
# Run App

if __name__ == '__main__':
    app.run(debug=True)