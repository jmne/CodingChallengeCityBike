#  Copyright (c) 2022 by jmne.
#  File: prepare_data.py
import pandas as pd


def prep(file="", remove_outliers=False, selectors=None):
    df = pd.read_csv(file)
    if selectors is not None:
        if len(selectors) > 0:
            df = df[selectors]
    df = df.replace(to_replace={"usertype": {"Customer": 0, "Subscriber": 1}})
    if remove_outliers is True:
        df = handle_outliers(df)
    # insert column in dataframe
    # df.insert(0, "usertype_pred", -1)
    df = df.dropna()
    df.info()
    return df


def handle_outliers(df):
    for column in df[["tripduration", "birth year"]].columns:
        q1 = df[column].quantile(0.05)
        q3 = df[column].quantile(0.95)
        iqr = q3 - q1
        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df
