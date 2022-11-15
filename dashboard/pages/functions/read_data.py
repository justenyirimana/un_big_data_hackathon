import pandas as pd


def read_data():
    """
    Reads in the clean_rw_food_prices.csv file
    """
    df = pd.read_csv("data\clean_rw_food_prices.csv")
    df["period"] = (
        pd.to_datetime(df.date).dt.to_period("M").astype(str)
    )  # converts the date column monthly period

    return df
