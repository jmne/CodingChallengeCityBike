#  Copyright (c) 2022 by jmne.
#  File: merge_csv.py

import glob
import os

# import necessary libraries
import pandas as pd

global csv_files


def merge():
    # use glob to get all the csv files
    # in the folder
    path = "../resources"
    files = glob.glob(os.path.join(path, "*.csv"))
    print(files)

    # joining files with concat and read_csv
    df = pd.concat(map(pd.read_csv, files), ignore_index=True)
    df.to_csv("../resources/merged_data.csv", encoding='utf-8', index=False)
