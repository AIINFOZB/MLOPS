import pandas as pd
import numpy as np
import subprocess
import shlex

# 1. Download and unpack dataset from Kaggle
print("Downloading datasets from Kaggle..")
subprocess.call(shlex.split('sudo sh kaggle.sh'))

# 2. Load dataset
print("Loading datasets from csv..")
test_df = pd.read_csv("test/test.csv", sep=",")
train_df = pd.read_csv("train/train.csv", sep=",")

train_rows = train_df.shape[0]
train_cols = train_df.shape[1]

test_rows = test_df.shape[0]
test_cols = test_df.shape[1]

train_df['date']= pd.to_datetime(train_df['date'])
test_df['date']= pd.to_datetime(test_df['date'])

# 3. Add some noise
mu, sigma = 0, 0.1 
print("Adding noise to datasets..")

# creating a noise with the same dimension as the train dataset excluding date column
noise_train = np.random.normal(mu, sigma, [train_rows, train_cols-1]) 

# creating a noise with the same dimension as the test dataset excluding date column
noise_test = np.random.normal(mu, sigma, [test_rows, test_cols-1]) 

# add noise to columns 1-4 of train dataset
train_df.iloc[:,1:5] = train_df.iloc[:,1:5] + noise_train

# add noise to columns 1-4 of test dataset
test_df.iloc[:,1:5] = test_df.iloc[:,1:5] + noise_test

# 4. Saving datasets with noise
train_df.to_csv("train/train.csv", sep=",", encoding='utf-8', index=False)
test_df.to_csv("test/test.csv", sep=",", encoding='utf-8', index=False)

print("Datasets created successfully!")
