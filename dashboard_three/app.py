import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = px.data.iris()

app.layout = html.Div([
    html.H1("Dashboard Interativo com Dash"),
    html.Label("Selecione uma espécie:"),
    dcc.Dropdown(
        id='dropdown-species',
        options=[{'label': species, 'value': species} for species in df['species'].unique()],
        value='setosa'
    ),
    html.Label("Selecione o intervalo de comprimento da sépala:"),
    dcc.RangeSlider(
        id='slider-sepal-length',
        min=df['sepal_length'].min(),
        max=df['sepal_length'].max(),
        step=0.1,
        value=[df['sepal_length'].min(), df['sepal_length'].max()],
        marks={i: str(i) for i in range(int(df['sepal_length'].min()), int(df['sepal_length'].max()) + 1)}
    ),
    dcc.Graph(id='graph-output')
])

@app.callback(
    Output('graph-output', 'figure'),
    [Input('dropdown-species', 'value'),
     Input('slider-sepal-length', 'value')]
)
def update_graph(selected_species, selected_sepal_length):
    filtered_df = df[(df['species'] == selected_species) & 
                     (df['sepal_length'] >= selected_sepal_length[0]) & 
                     (df['sepal_length'] <= selected_sepal_length[1])]
    
    fig = px.scatter(filtered_df, x='sepal_width', y='petal_length', color='species',
                     title=f'Especie: {selected_species} com Comprimento da Sepala Entre {selected_sepal_length[0]} e {selected_sepal_length[1]}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
