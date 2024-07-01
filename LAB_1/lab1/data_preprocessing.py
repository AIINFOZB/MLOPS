import pandas as pd
from sklearn.preprocessing import StandardScaler


def scale_df(df: pd.DataFrame) -> pd.DataFrame:
# applies standard scaling to the dataframe passed as a parameter
    df = df.dropna()
    scaler = StandardScaler()
    df.iloc[:,1:5]= scaler.fit_transform(df.iloc[:,1:5])
    return df

print("Preprocessing the data..")

train_df = pd.read_csv('./train/train.csv', sep=',')
train_df = scale_df(train_df)
train_df.to_csv('./train/train_preprocessed.csv', sep=',', encoding='utf-8', index=False)

test_df = pd.read_csv('./test/test.csv', sep=',')
test_df = scale_df(test_df)
test_df.to_csv('./test/test_preprocessed.csv', sep=',', encoding='utf-8', index=False)
