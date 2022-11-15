from dash import dcc, html


def create_dpdn(**kwargs):
    """
    Builds a drop down menu
    """
    kwargs.setdefault("margin_left", None)

    dpdn = html.Div(
        [
            html.H5(kwargs["header"]),
            dcc.Dropdown(
                id=kwargs["id"], options=kwargs["options"], value=kwargs["value"],
            ),
        ],
        style={
            "width": kwargs["width"],
            "margin-left": kwargs["margin_left"],
        },  # width: Adjusts the width of the div
    )
    return dpdn
