#  Copyright (c) 2022 by jmne.
#  File: decision_tree.py

import time

from sklearn.linear_model import LogisticRegression


# train model
def train_model(df):
    """
    Trains a logistic regression model on the given dataframe.

    Args:
        df: write your description
    """
    start_time = time.time()
    print("Starting to train Logistic Regression model...")

    # split data
    x_train = df[["birth year", "gender", "tripduration"]]
    y_train = df["usertype"]

    # define model
    # Decision Trees
    lr = LogisticRegression()

    # fit the classifier
    lr.fit(x_train, y_train)

    print("Time to train model (Logistic Regression):", round(time.time() - start_time, 2), "seconds")

    return lr


class LogisticRegressionModel:
    def __init__(self, df):
        """
        Initializes the model with the given dataframe

        Args:
            self: write your description
            df: write your description
        """
        self.df = df
        self.model = train_model(df)

    # predict values
    def predict(self, df):
        """
        Predicts the class for the given dataframe.

        Args:
            self: write your description
            df: write your description
        """
        start_time = time.time()
        pre = self.model.predict(df[["birth year", "gender", "tripduration"]])
        print("Time to predict data:", round(time.time() - start_time, 2), "seconds")
        return pre
