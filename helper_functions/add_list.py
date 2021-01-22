import pandas as pd
import numpy as np


#def day_month_year(df, column):
    #df =df.copy()
    #df["day"] = df[column].dt.day
    #df["month"] = df[column].dt.month
    #df["year"] = df[column].dt.year
    #return df

def add_list(df, series, name):
    df = df.copy()
    series = pd.Series(series)
    df[name] = series
    return df

#if __name__ == "__main__":
    #add_list.main()