#!/bin/bash

pip install -q kaggle
mkdir -p ~/.kaggle
cp kaggle.json ~/.kaggle/
ls ~/.kaggle
chmod 600 /root/.kaggle/kaggle.json

kaggle datasets download --force -d sumanthvrao/daily-climate-time-series-data -p kaggle/climate

unzip kaggle/climate/daily-climate-time-series-data
mkdir -p test; mv DailyDelhiClimateTest.csv test/test.csv
mkdir -p train; mv DailyDelhiClimateTrain.csv train/train.csv
