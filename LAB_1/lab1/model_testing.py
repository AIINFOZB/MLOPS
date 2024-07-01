import pickle
import pandas as pd
from sklearn.metrics import r2_score

print("Testing the model..")

with open('model.pkl', 'rb') as file:
    pickle_model = pickle.load(file)

test_df = pd.read_csv('./test/test_preprocessed.csv', sep=',')

test_y = test_df['meanpressure']
test_X = test_df.drop('meanpressure', axis=1)
test_X = test_df.drop('date', axis=1)

predict = pickle_model.predict(test_X)
print(test_y)

r2 = r2_score(test_y, predict)
print("Model test accuracy is: {0:.2f} %".format(100 * r2))
