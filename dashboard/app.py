import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

# from pages.overview_test import *
from pages.home import *

# from pages.data_source import *
from sidebar import *

# PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

app = dash.Dash(
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],
)

content = html.Div(id="page-content", className="content")

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

with open(("dashboard/pages/data_source.md"), "r") as file:
    data_source_md = file.read()

# set the content according to the current pathname
@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def render_page_content(pathname):
    if pathname == "/":
        return layout
    elif pathname == "/page_2":
        return html.Div(
            [dcc.Markdown(data_source_md)],
            style={
                "margin-left": "2rem",
                "margin-right": "1rem",
                "padding": "2rem 1rem",
            },
        )
    # elif pathname == "/page_3":
    #     return html.P("Work in progress ...")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True)
