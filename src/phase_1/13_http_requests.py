import requests
import json

url = "https://api.agify.io/?name=andrew"
response = requests.get(url)

data = response.json()

print(data["age"])