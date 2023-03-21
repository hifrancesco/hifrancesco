import json
import os
import requests
from dotenv import load_dotenv


load_dotenv()

url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"
querystring = {"lat": "53.483959", "lon": "-2.244644", "units": "metric", "lang": "en"}

headers = {
    "X-RapidAPI-Key": os.getenv('API_KEY'),
    "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Parse the JSON response
data = json.loads(response.text)

# Extract the relevant information from the JSON response
city_name = data["city_name"]
country_code = data["country_code"]
timezone = data["timezone"]

# Get the list of forecast data points
forecast_data = data["data"]

# Create a markdown-formatted string to display the forecast data
output = f"\n\n# Weather Forecast for {city_name}, {country_code}\n\n"
output += f"Timezone: {timezone}\n\n"

for forecast in forecast_data:
    time = forecast["timestamp_utc"]
    temperature = forecast["temp"]
    weather_description = forecast["weather"]["description"]
    output += f"**{time}:** | {temperature}°C | {weather_description}\n"

# Write the output to a markdown file
with open("README.md", "a") as f:
    f.write(output)