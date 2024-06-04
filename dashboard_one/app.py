import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City")

app.layout = html.Div(
    children=[
        html.H1(children="Hello Dash"),
        html.Div(children="Dash: A web application framework for Python."),
        html.Div(children="Here is a bar chart:"),
        dcc.Graph(figure=fig),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)