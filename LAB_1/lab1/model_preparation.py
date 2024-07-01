import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

print("Preparing the model..")

train_df = pd.read_csv('./train/train_preprocessed.csv', sep=',')

train_y = train_df['meanpressure']
train_X = train_df.drop('meanpressure', axis=1)
train_X = train_df.drop('date', axis=1)

model = LinearRegression()
model.fit(train_X, train_y)

with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
