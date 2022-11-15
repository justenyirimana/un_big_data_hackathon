import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def empty_plot(text):
    """
    Returns an empty plot with a centered text.
    """
    fig = go.Figure()
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis={"visible": False},
        yaxis={"visible": False},
        annotations=[
            {
                "text": text,
                "xref": "paper",
                "yref": "paper",
                "showarrow": False,
                "font": {"size": 20},
            }
        ],
    )

    return fig


def create_filtered_indicator(df, **kwargs):
    """
    Creates the indicator after filtering the camp and the period
    """
    fig = go.Figure(
        go.Indicator(
            mode="delta",
            value=df[
                (df.period == kwargs["yr"])
                & (df.market == kwargs["market"])
                & (df.commodity == kwargs["commodity"])
            ]["price"].iloc[0],
            delta={
                "reference": df["price"].iloc[
                    df[
                        (df.period == kwargs["yr"])
                        & (df.market == kwargs["market"])
                        & (df.commodity == kwargs["commodity"])
                    ].index.values.astype(int)[0]
                    - 1
                ],
                "relative": True,
                "valueformat": ".2%",
                "font": {"size": 15, "family": "Crimson Text"},
            },
            # relative = True means show percentage. relative = False means show new - old, hence why we don't see the % sign when it is set to False
            # ask stackoverflow how to format % change
        )
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        margin_b=30,  # padding, moves the indicator close the amount
        # width = 100,
        # height = 0
    )
    return fig


def create_px_line(**kwargs):
    """
    Creates the line plot for the commodity prices
    """
    fig = px.line(
        kwargs["df"][
            (
                kwargs["df"].commodity.isin(
                    ["Oil (palm)", "Sugar", "Cassava flour", "Potatoes (Irish)"]
                )
            )
            & (kwargs["df"].market == kwargs["camp"])
            & (pd.to_datetime(kwargs["df"].date).dt.year >= 2021)
        ],
        x="date",
        y="price",
        color="commodity",
        markers=True,
        color_discrete_sequence=["#AD5105", "#FAE4D2", "#0395AD", "#00D6FA"],
        title=kwargs["title"],
        labels={"commodity": "Commodities"},
    )

    fig.add_vline(x="2022-04-04", line_width=3, line_dash="dash", line_color="#000000")
    fig.add_vline(x="2022-06-10", line_width=3, line_dash="dash", line_color="#000000")
    fig.add_vline(x="2022-08-08", line_width=3, line_dash="dash", line_color="#000000")
    fig.add_vline(x="2022-10-08", line_width=3, line_dash="dash", line_color="#A9A9A9")

    fig.update_layout(
        xaxis_title="Period",
        yaxis_title="Prices (RWF)",
        xaxis=dict(
            showline=True,
            linecolor="rgb(204, 204, 204)",
            linewidth=2,
            ticks="outside",
            tickfont=dict(family="Arial", size=12, color="rgb(82, 82, 82)",),
        ),
        yaxis=dict(
            showline=True,
            linecolor="rgb(204, 204, 204)",
            linewidth=2,
            showgrid=True,
            gridcolor="rgb(204, 204, 204)",
        ),
        autosize=False,
        showlegend=True,
        plot_bgcolor="white",
    )

    # add annotation
    fig.add_annotation(
        dict(
            font=dict(color="black", size=13),
            x="2022-01-01",
            y=-0.2,
            showarrow=False,
            text="""NB: The verticle lines represent fuel price changes, the dark lines represent an increase in prices while the gray lines mean a decrease in prices.""",
            textangle=0,
            xanchor="left",
            xref="paper",
            yref="paper",
        )
    )

    # fig.update_traces(line_color="#753918", line_width=2)

    # fig.update_xaxes(dtick="M1", tickformat="%b-%y")
    return fig
    # fig.show()

