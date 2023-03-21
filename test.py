import json

# Load the contents of the JSON file as a string
with open('data.json') as f:
    json_str = f.read()

# Replace all single quotes with double quotes
json_str = json_str.replace("'", "\"")

# Load the modified JSON string using json.loads
data = json.loads(json_str)

# Now you can access the data as a Python dictionary
print(data['city_name'])
