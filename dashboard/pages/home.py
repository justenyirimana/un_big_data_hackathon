import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
from dash import Input, Output, callback, dcc, html

import plotly.express as px
from .functions.dpdn import *
from .functions.read_data import read_data
from .functions.figures import *
from .functions.card import *


############ colors and fonts

colors = {
    "background": "#EBCF8A",  # EBCF8A, #AA892C
    "bodyColor": "#F9F1DC",
    "card_title": "#808080",
    "line_color": "#753918",
}

fontsize = {"card_figure": 25, "card_footer": 12}

# reads in the food prices data
df = read_data()

############ dropdown menus

yr_dpdn = create_dpdn(
    header="Select period:",
    id="yr-dpdn",
    options=df.period.unique(),
    value="2022-09",
    width="30%",
)

cmp_dpdn = create_dpdn(
    header="Select market:",
    id="cmp-dpdn",
    # options=np.append("All", df.market.unique()),
    options=df.market.unique(),
    value="Mahama (Camp)",  # Mahama as default as it is largest in terms of refugees
    width="44%",
    margin_left="-250px",
)

currency_dpdn = create_dpdn(
    header="Select currency:",
    id="currency-dpdn",
    # options=np.append("All", df.market.unique()),
    options=df.currency.unique(),
    value="RWF",  # Mahama as default as it is largest in terms of refugees
    width="40%",
    margin_left="-450px",
)

############ cards

sugar_card = build_prices_card(
    card_title="Sugar",
    card_title_color=colors["card_title"],
    h2_id="sugar-figure",
    card_font_size=fontsize["card_figure"],
    graph_id="sugar-icon",
    card_footer_font_size=fontsize["card_footer"],
)

potato_card = build_prices_card(
    card_title="Potatoes (Irish)",
    card_title_color=colors["card_title"],
    h2_id="potato-figure",
    card_font_size=fontsize["card_figure"],
    graph_id="potato-icon",
    card_footer_font_size=fontsize["card_footer"],
)

cassava_card = build_prices_card(
    card_title="Cassava flour",
    card_title_color=colors["card_title"],
    h2_id="cassava-figure",
    card_font_size=fontsize["card_figure"],
    graph_id="cassava-icon",
    card_footer_font_size=fontsize["card_footer"],
)

palm_oil_card = build_prices_card(
    card_title="Oil (palm)",
    card_title_color=colors["card_title"],
    h2_id="palm-oil-figure",
    card_font_size=fontsize["card_figure"],
    graph_id="palm-oil-icon",
    card_footer_font_size=fontsize["card_footer"],
)

############ Graphs

commodities_graph = dbc.Card(
    dcc.Graph(id="commodities-graph", style={"width": "70rem", "height": "35rem"}),
    style={"width": "75.7em", "height": "35.5rem"},
)

############ Layout

layout = dbc.Container(
    [
        html.Div(
            [  # This was supposed to be a row followed by a column like the rest of the content in this container. I used div because I wanted the Hr to be on the same line
                html.H2(
                    "Market prices dashboard"
                )  # , style={'textAlign': 'center'})#h1 is like a header (similar to # in markdown)
            ]
        ),
        html.Hr(),  # draws horizontal line
        dbc.Row(
            [
                dbc.Col(yr_dpdn, width=4),  # adjusts the width of the column
                dbc.Col(cmp_dpdn, width=4),  #
                dbc.Col(currency_dpdn, width=4),  #
            ],
            className="g-0",  # this also helps with reducing space between the two columns
        ),
        html.Br(),  # puts space between the two rows
        dbc.Row(
            [
                dbc.Col(palm_oil_card),
                dbc.Col(sugar_card),
                dbc.Col(cassava_card),
                dbc.Col(potato_card),
            ],
            className="g-0",
        ),
        html.Br(),  # puts space between the two rows
        dbc.Row(
            [
                dbc.Col(commodities_graph),
                #         # dbc.Col(accounts_receivable_card),
                #         # dbc.Col(accounts_payable_card),
                #         # dbc.Col(net_profit_card),
            ],
            className="g-0",
        ),
    ]
)


############ callbacks

##### Sugar prices callbacks


@callback(
    Output(component_id="sugar-figure", component_property="children"),
    Input(component_id="yr-dpdn", component_property="value"),
    Input(component_id="cmp-dpdn", component_property="value"),
)
def update_sugar_card(
    selected_yr, selected_camp
):  # the function argument comes from the component property of the Input
    if (
        df[
            (df.period == selected_yr)
            & (df.market == selected_camp)
            & (df.commodity == "Sugar")
        ].shape[0]
        == 0
    ):
        return f"NA"
    else:
        return f"{df[(df.period == selected_yr) & (df.market == selected_camp) & (df.commodity == 'Sugar')]['price'].iloc[0]:,.2f}/KG"  # .iloc[0]/1000000000


@callback(
    Output("sugar-icon", "figure"),
    Input(component_id="yr-dpdn", component_property="value"),
    Input(component_id="cmp-dpdn", component_property="value"),
)
def update_sugar_graph(selected_yr, selected_camp):
    if (
        min(df.period.unique()) == selected_yr
    ):  # if it's the earliest period for any market, return na
        fig = empty_plot("<b>NA<b>")

    elif (
        df[
            (df.period == selected_yr)
            & (df.market == selected_camp)
            & (df.commodity == "Sugar")
        ].shape[0]
        == 0
    ):
        fig = empty_plot("<b>NA<b>")
    else:
        filtered_data = (
            df[(df.market == selected_camp) & (df.commodity == "Sugar")]
            .sort_values("date")
            .reset_index(drop=True)
        )
        fig = create_filtered_indicator(
            df=filtered_data, yr=selected_yr, market=selected_camp, commodity="Sugar"
        )
    return fig


##### potato prices callbacks


@callback(
    Output(component_id="potato-figure", component_property="children"),
    Input(component_id="yr-dpdn", component_property="value"),
    Input(component_id="cmp-dpdn", component_property="value"),
)
def update_potatoes_card(
    selected_yr, selected_camp
):  # the function argument comes from the component property of the Input
    if (
        df[
            (df.period == selected_yr)
            & (df.market == selected_camp)
            & (df.commodity == "Potatoes (Irish)")
        ].shape[0]
        == 0
    ):
        return f"NA"
    else:
        return f"{df[(df.period == selected_yr) & (df.market == selected_camp) & (df.commodity == 'Potatoes (Irish)')]['price'].iloc[0]:,.2f}/KG"  # .iloc[0]/1000000000


@callback(
    Output("potato-icon", "figure"),
    Input(component_id="yr-dpdn", component_property="value"),
    Input(component_id="cmp-dpdn", component_property="value"),
)
def update_sugar_graph(selected_yr, selected_camp):
    if (
        min(df.period.unique()) == selected_yr
    ):  # if it's the earliest period for any market, return na
        fig = empty_plot("<b>NA<b>")

    elif (
        df[
            (df.period == selected_yr)
            & (df.market == selected_camp)
            & (df.commodity == "Potatoes (Irish)")
        ].shape[0]
        == 0
    ):
        fig = empty_plot("<b>NA<b>")
    else:
        filtered_data = (
            df[(df.market == selected_camp) & (df.commodity == "Potatoes (Irish)")]
            .sort_values("date")
            .reset_index(drop=True)
        )
        fig = create_filtered_indicator(
            df=filtered_data,
            yr=selected_yr,
            market=selected_camp,
            commodity="Potatoes (Irish)",
        )
    return fig


##### cassava flour prices callbacks


@callback(
    Output(component_id="cassava-figure", component_property="children"),
    Input(component_id="yr-dpdn", component_property="value"),
    Input(component_id="cmp-dpdn", component_property="value"),
)
def update_cassava_flour_card(
    selected_yr, selected_camp
):  # the function argument comes from the component property of the Input
    if (
        df[
            (df.period == selected_yr)
            & (df.market == selected_camp)
            & (df.commodity == "Cassava flour")
        ].shape[0]
        == 0
    ):
        return f"NA"
    else:
        return f"{df[(df.period == selected_yr) & (df.market == selected_camp) & (df.commodity == 'Cassava flour')]['price'].iloc[0]:,.2f}/KG"  # .iloc[0]/1000000000


@callback(
    Output("cassava-icon", "figure"),
    Input(component_id="yr-dpdn", component_property="value"),
    Input(component_id="cmp-dpdn", component_property="value"),
)
def update_cassava_flour_graph(selected_yr, selected_camp):
    if (
        min(df.period.unique()) == selected_yr
    ):  # if it's the earliest period for any market, return na
        fig = empty_plot("<b>NA<b>")

    elif (
        df[
            (df.period == selected_yr)
            & (df.market == selected_camp)
            & (df.commodity == "Cassava flour")
        ].shape[0]
        == 0
    ):
        fig = empty_plot("<b>NA<b>")
    else:
        filtered_data = (
            df[(df.market == selected_camp) & (df.commodity == "Cassava flour")]
            .sort_values("date")
            .reset_index(drop=True)
        )
        fig = create_filtered_indicator(
            df=filtered_data,
            yr=selected_yr,
            market=selected_camp,
            commodity="Cassava flour",
        )
    return fig


##### palm oil prices callbacks


@callback(
    Output(component_id="palm-oil-figure", component_property="children"),
    Input(component_id="yr-dpdn", component_property="value"),
    Input(component_id="cmp-dpdn", component_property="value"),
)
def update_palm_oil_card(
    selected_yr, selected_camp
):  # the function argument comes from the component property of the Input
    if (
        df[
            (df.period == selected_yr)
            & (df.market == selected_camp)
            & (df.commodity == "Oil (palm)")
        ].shape[0]
        == 0
    ):
        return f"NA"
    else:
        return f"{df[(df.period == selected_yr) & (df.market == selected_camp) & (df.commodity == 'Oil (palm)')]['price'].iloc[0]:,.2f}/L"  # .iloc[0]/1000000000


@callback(
    Output("palm-oil-icon", "figure"),
    Input(component_id="yr-dpdn", component_property="value"),
    Input(component_id="cmp-dpdn", component_property="value"),
)
def update_palm_oil_graph(selected_yr, selected_camp):
    if (
        min(df.period.unique()) == selected_yr
    ):  # if it's the earliest period for any market, return na
        fig = empty_plot("<b>NA<b>")

    elif (
        df[
            (df.period == selected_yr)
            & (df.market == selected_camp)
            & (df.commodity == "Oil (palm)")
        ].shape[0]
        == 0
    ):
        fig = empty_plot("<b>NA<b>")
    else:
        filtered_data = (
            df[(df.market == selected_camp) & (df.commodity == "Oil (palm)")]
            .sort_values("date")
            .reset_index(drop=True)
        )
        fig = create_filtered_indicator(
            df=filtered_data,
            yr=selected_yr,
            market=selected_camp,
            commodity="Oil (palm)",
        )
    return fig


@callback(
    Output("commodities-graph", "figure"),
    Input(component_id="cmp-dpdn", component_property="value"),
)
def update_commodities_graph(selected_camp):
    fig = create_px_line(df=df, camp=selected_camp, title="Commodity prices over time")
    return fig

