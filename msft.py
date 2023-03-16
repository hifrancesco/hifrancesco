import requests
import json

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"function":"TIME_SERIES_WEEKLY_ADJUSTED","symbol":"MSFT","datatype":"json"}

headers = {
	"X-RapidAPI-Key": "a1fd8c53f7msh14dffeb471fe4eep100834jsn5acdd4a91ed6",
	"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

# Parse the JSON data into a Python dictionary
data = json.loads(response.text)

# Extract the weekly adjusted time series data into a list of dictionaries
weekly_data = []
for date, values in data["Weekly Adjusted Time Series"].items():
    weekly_data.append({
        "date": date,
        "open": values["1. open"],
        "high": values["2. high"],
        "low": values["3. low"],
        "close": values["4. close"],
        "volume": values["6. volume"]
    })

# Generate markdown-formatted output
output = "# Weekly Adjusted Time Series for MSFT\n\n"
output += "| Date | Open | High | Low | Close | Volume |\n"
output += "| ---- | ---- | ---- | --- | ----- | ------ |\n"
for item in weekly_data:
    output += f"| {item['date']} | {item['open']} | {item['high']} | {item['low']} | {item['close']} | {item['volume']} |\n"

# Write output to file
with open("msft_weekly_data.md", "w") as f:
    f.write(output)