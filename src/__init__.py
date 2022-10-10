#  Copyright (c) 2022 by jmne.
#  File: __init__.py

import time

import analytics.plot_boxplot as pb
import analytics.plot_correlation_matrix as pcm
import analytics.plot_histogram as ph
import analytics.plot_scatter as ps
import model.decision_tree as dt
import model.evaluate_models as evm
import model.logistic_regression as lr
import utils.prepare_data as pd

if __name__ == '__main__':
    start_time = time.time()

    # load and prepare data
    df = pd.prep(file="../resources/201808-citibike-tripdata.csv",
                 selectors=["birth year", "gender", "tripduration", "usertype"],
                 remove_outliers=False)

    # Print subscriber to customer ratio
    cust = df[(df.usertype == 0)]
    subs = df[(df.usertype == 1)]
    print("Customer Ratio: {}:{} = {}%".format
          (len(cust.index), len(df.index), round(len(cust.index) / len(df.index) * 100, 2)))

    # plot correlation matrix
    pcm.plot(df)

    # plot histogram
    ph.plot(df)

    # plot scatter (+density)
    ps.plot(df)
    ps.plot_with_density(df)

    # plot boxplot
    pb.plot(df)

    # evaluate models
    evm.model(df)

    # predict values
    dtc = dt.DecisionTreeModel(df)
    lr = lr.LogisticRegressionModel(df)

    df2 = pd.prep(file="../resources/201809-citibike-tripdata.csv",
                  selectors=["birth year", "gender", "tripduration", "usertype"],
                  remove_outliers=False)
    df2["prediction_dt"] = dtc.predict(df2)
    df2["prediction_lr"] = lr.predict(df2)
    print(df2)
    print("\n Evaluating DT...")
    evm.evaluate(df2["usertype"], df2["prediction_dt"])
    print("\n Evaluating LR...")
    evm.evaluate(df2["usertype"], df2["prediction_lr"])

    # print execution time
    print("\n--- calculated %s minutes ---" % round((time.time() - start_time) / 60, 2))

    exit(0)
