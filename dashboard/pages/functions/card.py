from dash import dcc, html
import dash_bootstrap_components as dbc


def build_prices_card(**kwargs):
    """
    Builds the commodity prices cards
    """
    card = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H6(
                        kwargs["card_title"],
                        className="card-title",
                        style={
                            "textAlign": "center",
                            "color": kwargs["card_title_color"],
                        },
                    ),
                    # html.H6("Card subtitle", className="card-subtitle"),
                    html.Br(),
                    html.H2(
                        children="",
                        id=kwargs["h2_id"],
                        style={
                            "textAlign": "center",
                            "fontSize": kwargs["card_font_size"],
                            "font-family": "Crimson Text",
                            "font-weight": "bold",
                        },
                    ),
                    dcc.Graph(
                        id=kwargs["graph_id"],
                        style={
                            "height": 50,
                            "width": 70,
                            "margin-left": "auto",
                            "margin-right": "auto",
                        }
                        # the height and width control the size of the indicator
                    ),  # to center the graph you must set margin-left and margin-right to auto
                    html.H6(
                        "vs previous 30 days*",
                        className="card-text text-muted",
                        style={
                            "textAlign": "center",
                            "fontSize": kwargs["card_footer_font_size"],
                        },
                    ),
                ]
            ),
            # dbc.CardFooter("This is the footer"),
        ],
        style={"width": "15rem", "height": "13rem"},
    )

    return card
