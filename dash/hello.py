from dash import Dash, html

# Initialize App

app = Dash(__name__)

# App Layout

app.layout = html.Div([
    html.Div(children='Hello Dash')
])

if __name__ == '__main__':
    app.run(debug=True)