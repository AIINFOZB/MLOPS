import pandas as pd
import argparse
from sklearn.neighbors import KNeighborsClassifier
import pickle

def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--train-path",
                                 required=True, 
                                 help="Path to train dataset")
    argument_parser.add_argument("--model-path",
                                 required=True, 
                                 help="Path to save trained model")
    args = argument_parser.parse_args()
    
    train_data = pd.read_csv(args.train_path)

    X_train = train_data.drop('variety', axis=1)

    model = KNeighborsClassifier()

    model.fit(X_train, train_data['variety'])

    with open(args.model_path, 'wb') as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    main()