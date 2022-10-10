#  Copyright (c) 2022 by jmne.
#  File: evaluate_models.py

import time

import pandas as pds
from matplotlib import pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split


def model(df):
    """
    Run the processing models on the data.

    Args:
        df: write your description
    """
    # split data into train and test
    x = df[["birth year", "gender", "tripduration"]]
    y = df["usertype"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.6, random_state=0)

    models = {}

    # define models

    # Logistic Regression
    from sklearn.linear_model import LogisticRegression
    models['Logistic Regression'] = LogisticRegression()

    # Support Vector (takes a while)
    # from sklearn.svm import LinearSVC
    # models['Support Vector'] = LinearSVC(verbose=1)

    # Decision Trees
    from sklearn.tree import DecisionTreeClassifier
    models['Decision Trees'] = DecisionTreeClassifier()

    # Random Forest
    # from sklearn.ensemble import RandomForestClassifier
    # models['Random Forest'] = RandomForestClassifier(max_depth=2, random_state=0)

    # Naive Bayes
    from sklearn.naive_bayes import GaussianNB
    models['Naive Bayes'] = GaussianNB()

    # K-Nearest Neighbors (takes a while)
    # from sklearn.neighbors import KNeighborsClassifier
    # models['K-Nearest Neighbor'] = KNeighborsClassifier()

    # Machine Learning (takes a while)
    # from sklearn.neural_network import MLPClassifier
    # models['Machine Learning'] = MLPClassifier(verbose=1, max_iter=10)

    accuracy, precision, recall, times = {}, {}, {}, {}

    # create figure and axis objects with subplots()
    fig, axs = plt.subplots(round(len(df.columns) / 2), 2)
    fig.suptitle('Confusion Matrix of Models', fontsize=20)
    a = 0
    b = 0
    fig.set_size_inches(13, 10)
    h = None

    # iterate over models and create evaluations
    for key in models.keys():
        start_time = time.time()

        # print processing model
        print("Processing: " + key)

        # fit the classifier
        models[key].fit(x_train, y_train)

        # make predictions
        predictions = models[key].predict(x_test)

        # calculate metrics
        accuracy[key] = accuracy_score(predictions, y_test)
        precision[key] = precision_score(predictions, y_test)
        recall[key] = recall_score(predictions, y_test)
        times[key] = time.time() - start_time

        # generate confusion matrix
        cf = confusion_matrix(predictions, y_test)

        cm_display = ConfusionMatrixDisplay(confusion_matrix=cf, display_labels=["Customer", "Subscriber"])
        h = cm_display.plot(ax=axs[a, b], colorbar=False)
        axs[a, b].set_title(key)

        # select the right subplot
        if b == 0:
            b = 1
        else:
            a += 1
            b = 0

    fig.colorbar(h.im_, ax=axs)
    plt.show()

    # print evaluation of models
    df_model = pds.DataFrame(index=models.keys(), columns=['Accuracy', 'Precision', 'Recall', 'Time'])
    df_model['Accuracy'] = accuracy.values()
    df_model['Precision'] = precision.values()
    df_model['Recall'] = recall.values()
    df_model['Time'] = times.values()

    print(df_model)


def evaluate(test, prediction):
    """
    Scores and displays the confusion matrix.

    Args:
        test: write your description
        prediction: write your description
    """
    # calculate metrics
    print("Accuracy:", round(accuracy_score(prediction, test), 4) * 100, "%")
    print("Precision:", round(precision_score(prediction, test), 4) * 100, "%")
    print("Recall:", round(recall_score(prediction, test), 4) * 100, "%")
    cm = confusion_matrix(prediction, test)
    cm_display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Customer", "Subscriber"])
    cm_display.plot()
    plt.show()
