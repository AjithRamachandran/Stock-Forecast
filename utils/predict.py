import pandas as pd
import numpy as np
from keras.engine.saving import model_from_json
from sklearn.preprocessing import MinMaxScaler
from tensorflow import get_default_graph
from keras import backend as K

from utils.common import length

scaler = MinMaxScaler(feature_range=(0, 1))

def init(model):
    json = 'models/bin/' + model + '.json'
    h5 = 'models/bin/' + model + '.h5'
    json_file = open(json, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(h5)
    loaded_model.compile(loss='mean_squared_error', optimizer='adam')
    graph = get_default_graph()
    return loaded_model, graph


def predict_ms():
    csv = 'assets/Microsoft.csv'
    global model, graph, last, df
    model, graph = init('microsoft_model')
    df = pd.read_csv(csv)
    df = df.set_index('Date')
    df = df.iloc[:, 10:11].values
    df = np.array(df)
    df = scaler.fit_transform(df)
    last = length(csv)
    x = [df[last - 60:last, 0]]
    x = np.array(x)
    x = x.reshape(1, x.shape[1], 1)
    pred = model.predict(x)
    K.clear_session()
    prediction = scaler.inverse_transform(pred)
    return prediction[0]


def predict_intel():
    csv = 'assets/Intel.csv'
    global model, graph, last, df
    model, graph = init('intel_model')
    df = pd.read_csv(csv)
    df = df.set_index('Date')
    df = df.iloc[:, 10:11].values
    df = np.array(df)
    df = scaler.fit_transform(df)
    last = length(csv)
    x = [df[last - 60:last, 0]]
    x = np.array(x)
    x = x.reshape(1, x.shape[1], 1)
    pred = model.predict(x)
    K.clear_session()
    prediction = scaler.inverse_transform(pred)
    return prediction[0]


def predict_apple():
    csv = 'assets/Apple.csv'
    global model, graph, last, df
    model, graph = init('apple_model')
    df = pd.read_csv(csv)
    df = df.set_index('Date')
    df = df.iloc[:, 10:11].values
    df = np.array(df)
    df = scaler.fit_transform(df)
    last = length(csv)
    x = [df[last - 60:last, 0]]
    x = np.array(x)
    x = x.reshape(1, x.shape[1], 1)
    pred = model.predict(x)
    K.clear_session()
    prediction = scaler.inverse_transform(pred)
    return prediction[0]
