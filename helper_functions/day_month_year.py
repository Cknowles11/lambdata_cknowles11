import pandas as pd

def day_month_year(df, column):
    df =df.copy()
    df["day"] = df[column].dt.day
    df["month"] = df[column].dt.month
    df["year"] = df[column].dt.year
    return df