# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, dash_table
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# ----------------- DATA ----------------
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

# ----------------- DATA TABLE----------------
app.layout = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])

# ----------------- FIGURE ----------------
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# ----------------- THE HTML ----------------
app.layout = html.Div(children=[

    html.H1(children='Machine learning project'),
    html.H2(children='Made with Dash, Python and scikit-learn'),
    html.H3(children='Machine learning course project as a part of my data science education.'),

    html.Div([
        html.Div('Example pandas dataframe as variable in the script', style={'color': 'blue', 'fontSize': 14}),
        html.P('Example : three features, 6 rows', className='my-class', id='my-p-element')
    ], style={'marginBottom': 50, 'marginTop': 25}),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

        html.Div([
        html.Div('Example external csv file as a Datatable component', style={'color': 'blue', 'fontSize': 14}),
        html.P('Example : five features, 8 rows', className='my-class', id='my-p-element')
    ], style={'marginBottom': 50, 'marginTop': 25}),

    dash_table.DataTable(
    df2.to_dict('records'),
    [{"name": i, "id": i} for i in df2.columns]
)

])

# ----------------- RUN ----------------
if __name__ == '__main__':
    app.run_server(debug=True)
