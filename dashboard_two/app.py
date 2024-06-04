import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app.layout = html.Div([

    html.H1("Gapminder Data", style={'text-align': 'center'}),
    dcc.Graph(id='gapminder',
              figure=px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent", hover_name="country",
                                log_x=True, size_max=60))
])

if __name__ == '__main__':
    app.run_server(debug=True)