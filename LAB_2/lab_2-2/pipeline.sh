#!/usr/bin bash

PY=$(which python3)

TRAIN="train"
TEST="test"
CSV_FILE_PATH_TRAIN="${TRAIN}/data.csv"
CSV_FILE_PATH_TEST="${TEST}/data.csv"
MODEL_PATH="model.pkl"


testSumcommandStatus () {
    status=$?
    if [ $status -ne 0 ]; then
    echo "Error occured in subcommand $1"
    exit $status
    fi
    
}

$PY -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt

# Step 1 - data creation
for FOLDER in $TRAIN $TEST
do
    mkdir -p $FOLDER
done
python3 data_creation.py --train-path $CSV_FILE_PATH_TRAIN --test-path $CSV_FILE_PATH_TEST
testSumcommandStatus "data_creation"

# Step 2 - data preprocessing
python3 data_preprocessing.py --train-path $CSV_FILE_PATH_TRAIN --test-path $CSV_FILE_PATH_TEST
testSumcommandStatus "data_preprocessing"

# Step 3 - model preparation
python3 model_preparation.py --train-path $CSV_FILE_PATH_TRAIN --model-path $MODEL_PATH
testSumcommandStatus "model_preparation"

# Step 4 - model testing
python3 model_testing.py --test-path $CSV_FILE_PATH_TEST --model-path $MODEL_PATH
testSumcommandStatus "model_testing"
