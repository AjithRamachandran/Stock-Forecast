import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from sklearn.preprocessing import MinMaxScaler
from keras.callbacks import EarlyStopping

from utils.common import length

csv = '../assets/Intel.csv'
scaler = MinMaxScaler(feature_range=(0, 1))

df = pd.read_csv(csv, header=0)
df = df.set_index('Date')
df = df[::-1]
df = df.iloc[:, 10:11].values

data = scaler.fit_transform(df)

X = []
y = []
for i in range(60, length(csv)):
    X.append(data[i-60:i, 0])
    y.append(data[i, 0])

X = np.array(X)
y = np.array(y)

X = X.reshape(X.shape[0], X.shape[1], 1)

model = Sequential()

model.add(LSTM(64, input_shape=(X.shape[1], 1), return_sequences=True))
model.add(Dropout(.1))
model.add(LSTM(64, return_sequences=True))
model.add(Dropout(.1))
model.add(LSTM(64))
model.add(Dropout(.1))
model.add(Dense(1))

model.summary()
early_stop = EarlyStopping(monitor='val_loss', patience=10, mode='auto')
model.compile(optimizer = 'adam', loss = 'mean_squared_error', metrics=['accuracy'])

model.fit(X, y, epochs=100, batch_size=32, callbacks=[early_stop])

model_json = model.to_json()
with open('bin/intel_model.json', 'w') as json_file:
    json_file.write(model_json)
model.save_weights('bin/intel_model.h5')