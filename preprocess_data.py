import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data():
    df = pd.read_csv("raw_data.csv")
    df = df.dropna()
    scaler = MinMaxScaler()
    df[["Temperature", "Wind Speed"]] = scaler.fit_transform(df[["Temperature", "Wind Speed"]])
    df.to_csv("processed_data.csv", index=False)

if __name__ == "__main__":
    preprocess_data()
