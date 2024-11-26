import requests
import pandas as pd
from datetime import datetime

API_KEY = "your_api_key"
CITY = "your_city"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data():
    response = requests.get(BASE_URL, params={"q": CITY, "appid": API_KEY, "units": "metric"})
    data = response.json()

    # Check for errors in the response
    if response.status_code != 200:
        print(f"Error: {data.get('message', 'Unknown error')}")
        return None

    weather = {
        "Temperature": data["main"]["temp"],
        "Humidity": data["main"]["humidity"],
        "Wind Speed": data["wind"]["speed"],
        "Weather Condition": data["weather"][0]["description"],
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Time": datetime.now().strftime("%H:%M:%S")
    }
    return weather

if __name__ == "__main__":
    weather_data = [fetch_weather_data() for _ in range(5)]
    weather_data = [wd for wd in weather_data if wd is not None]  # Filter out None responses
    df = pd.DataFrame(weather_data)
    df.to_csv("raw_data.csv", index=False)
