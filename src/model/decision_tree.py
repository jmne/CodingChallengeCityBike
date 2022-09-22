#  Copyright (c) 2022 by jmne.
#  File: decision_tree.py

import time

from sklearn.tree import DecisionTreeClassifier


# train model
def train_model(df):
    start_time = time.time()
    print("Starting to train Decision Tree model...")

    # split data
    x_train = df[["birth year", "gender", "tripduration"]]
    y_train = df["usertype"]

    # define model
    # Decision Trees
    dtc = DecisionTreeClassifier()

    # fit the classifier
    dtc.fit(x_train, y_train)

    print("Time to train model (Decision Tree):", round(time.time() - start_time, 2), "seconds")

    return dtc


class DecisionTreeModel:
    def __init__(self, df):
        self.df = df
        self.model = train_model(df)

    # predict values
    def predict(self, df):
        start_time = time.time()
        pre = self.model.predict(df[["birth year", "gender", "tripduration"]])
        print("Time to predict data:", round(time.time() - start_time, 2), "seconds")
        return pre
