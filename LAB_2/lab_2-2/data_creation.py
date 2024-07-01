import numpy as np
import pandas as pd
import argparse


URL = """
https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv
"""


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--train-path",
                                 required=True, 
                                 help="Path to train dataset")
    argument_parser.add_argument("--test-path",
                                 required=True, 
                                 help="Path to test dataset")
    args = argument_parser.parse_args()
    
    dataset = pd.read_csv(URL)

    num_samples = dataset.shape[0]
    rnd_indices = np.arange(0, num_samples)
    np.random.shuffle(rnd_indices)

    boundary = int(np.floor(num_samples*0.7))
    train_indices = rnd_indices[:boundary]
    test_indices = rnd_indices[boundary:]

    train_dataset = dataset.iloc[train_indices].copy()
    test_dataset = dataset.iloc[test_indices].copy()
    train_dataset.to_csv(args.train_path, index=False, sep=",")
    test_dataset.to_csv(args.test_path, index=False, sep=",")


if __name__ == "__main__":
    main()