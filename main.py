import requests
import json

from headers import *

url = "https://real-time-amazon-data.p.rapidapi.com/deals-v2"

querystring = {"country": "US", "categories": "eletronic", "min_product_star_rating":"ALL", "prince_range": "ALL", "discount_range": "ALL"}

headers = {
    "x-rapidapi-key": key,
    "x-rapidapi-host": host
}

response = requests.get(url, headers=headers, params=querystring)
response_json = response.json()

print(response_json)

with open("amazon_data_json", "w") as file:
    json.dump(response_json, file, indent=4)