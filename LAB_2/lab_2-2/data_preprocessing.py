import pandas as pd
import argparse
from sklearn.preprocessing import StandardScaler, LabelEncoder


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--train-path",
                                 required=True,
                                 help="Path to train dataset")
    argument_parser.add_argument("--test-path",
                                 required=True,
                                 help="Path to test dataset")
    args = argument_parser.parse_args()

    train_dataset = pd.read_csv(args.train_path)
    test_dataset = pd.read_csv(args.test_path)

    # Fill missing values with mean (numerical features)
    for col in train_dataset.columns:
        if train_dataset[col].dtype == 'float64':
            train_dataset[col].fillna(train_dataset[col].mean(), inplace=True)
            test_dataset[col].fillna(test_dataset[col].mean(), inplace=True)

    # Normalize numerical features
    scaler = StandardScaler()
    for feature in ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']:
        train_dataset[feature] = scaler.fit_transform(
            train_dataset[feature].values.reshape(-1, 1))
        test_dataset[feature] = scaler.transform(
            test_dataset[feature].values.reshape(-1, 1))

    # Encode categorical features
    encoder = LabelEncoder()
    train_dataset['variety'] = encoder.fit_transform(train_dataset['variety'])
    test_dataset['variety'] = encoder.transform(test_dataset['variety'])

    train_dataset.to_csv(args.train_path, index=False)
    test_dataset.to_csv(args.test_path, index=False)


if __name__ == "__main__":
    main()
