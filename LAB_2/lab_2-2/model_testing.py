import pandas as pd
import argparse
import pickle

def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--test-path",
                                 required=True, 
                                 help="Path to test dataset")
    argument_parser.add_argument("--model-path",
                                 required=True, 
                                 help="Path to save tests of model")
    args = argument_parser.parse_args()

    test_data = pd.read_csv(args.test_path)

    X_test = test_data.drop('variety', axis=1)

    with open(args.model_path, 'rb') as file: 
        model = pickle.load(file)

    score = model.score(X_test, test_data['variety'])
    print("Model test accuracy is: {0:.3f}".format(score))

    model.predict(X_test)

if __name__ == "__main__":
    main()
