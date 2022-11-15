from dash import html
import dash_bootstrap_components as dbc

sidebar = html.Div(
    [
        html.Div(
            [
                # width: 3rem ensures the logo is the exact width of the
                # collapsed sidebar (accounting for padding)
                # html.Img(src=PLOTLY_LOGO, style={"width": "3rem"}),
                html.H2(
                    "Menu"
                )  # , style={'color': '#753918'}),#uncoment to change color of this particular H2 element
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="fas fa-home me-2"), html.Span("Home")],
                    # <i class="fas fa-home-lg"></i>
                    # <i class="fa-solid fa-bowling-ball"></i>
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-database"),
                        html.Span("Data source"),
                    ],
                    href="/page_2",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)
