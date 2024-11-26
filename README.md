# Weather Pipeline Project

## Description
This project collects weather data using OpenWeatherMap API, preprocesses it, and trains a simple linear regression model to predict temperature.

## Files
- `collect_data.py`: Fetches weather data and saves it as `raw_data.csv`.
- `preprocess_data.py`: Preprocesses the raw data and saves it as `processed_data.csv`.
- `train_model.py`: Trains a linear regression model and saves it as `model.pkl`.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
