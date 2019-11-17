#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'attributesSet' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER numberOfAttributes
#  2. FLOAT supportThreshold
#
import pandas as pd
import collections

COL_NAME = ["age","sex","education","native-country","race", "marital-status","workclass","occupation","hours-per-week","income","capital-gain","capital-loss"]

def read_csv2df(file):
    df = pd.read_csv(file)
    df.columns = COL_NAME
    # for i in COL_NAME:
    #     df[i] = df[i].str.replace("\w+=", "")
    return df

def dfs(attr_dict, col_name, k, temp_list, res, target):
    if k <= 0:
        res.append(temp_list)
        return
    if len(col_name) < k:
        return
    for i in range(len(col_name)-k+1):
        col = col_name[i]
        for option, count in attr_dict[col].items():
            if count / 30162 >= target:
                dfs(attr_dict, col_name[i+1:], k-1, temp_list + [[col, option]], res, target)
    return

def attributesSet(numberOfAttributes, supportThreshold):
    # Write your code here
    df = read_csv2df('census.csv')
    attr_dict = collections.defaultdict(dict)
    # print(df)
    for col in COL_NAME:
        for val in df[col].unique():
            attr_dict[col][val] = (df[col] == val).sum()
    # print(attr_dict)
    attr_candidate = []
    dfs(attr_dict, COL_NAME, numberOfAttributes, [], attr_candidate, supportThreshold)
    # select rows
    res = []
    for option in attr_candidate:
        temp = df
        for attr, val in option:
            temp = temp[temp[attr]==val]
        if len(temp) / 30162 > supportThreshold:
            res.append(','.join([ele[1] for ele in option]))
    # print(res)
    return res


if __name__ == '__main__':