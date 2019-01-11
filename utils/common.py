import csv
import pandas as pd
import numpy as np
import json


def length(csv_name):
    input_file = open(csv_name, "r+")
    reader_file = csv.reader(input_file)
    value = len(list(reader_file))
    value = value-1
    return value


def get_param(csv):
    df = pd.read_csv(csv, header=0)
    df = df[::-1]
    df = df.head(100)
    X = df['Date']
    y = df['Adj_Close']
    X = np.array(X)
    y = np.array(y)
    return X, y


def create_table(csv):
    df = pd.read_csv(csv)
    df = df[::-1]
    df = df.head(5)
    df = df[['Date', 'Adj_Open', 'Adj_High', 'Adj_Low', 'Adj_Close']]
    dates = df[['Date']]
    dates = np.array(dates)
    table = df[['Adj_Open', 'Adj_High', 'Adj_Low', 'Adj_Close']]
    table = np.array(table)
    table = np.round(table, 2)
    final = np.concatenate((dates, table), axis=1)
    return final


def export_data(date):
    json_ = {'date': date}
    with open('assets/date.json', 'w') as outfile:
        json.dump(json_, outfile)
