"""
lambdata-GwenStacey - A collection of Data Science helper
functions.
"""

import pandas as pd
import numpy as np 

ZEROS = np.zeros(5)
ONES = np.ones(10)

def print_nulls(df):
    nulls = df.isna().sum()
    columns = df.columns
    for i, v in zip(columns, nulls):
        print(f"Total nulls for {i} is {v}")

#cname here is for column name, took i out of list to avoid
#confusion with the type
def list_to_column(df, lst, cname):
    series = pd.Series(lst)
    df[cname] = series

  
