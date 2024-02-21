from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Read data
df = pd.read_csv('../data/totals/1994_player_totals.csv')

# Initialize App
app = Dash(__name__)

# Layout

app.layout = html.Div([
    html.Div(children='App with Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=25),
    dcc.Graph(figure=px.histogram(df, x='Pos', y='PTS', histfunc='avg'))
])

# Run App

if __name__ == '__main__':
    app.run(debug=True)