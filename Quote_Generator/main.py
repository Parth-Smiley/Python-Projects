import requests
import os
from dotenv import load_dotenv,dotenv_values

load_dotenv(dotenv_path="../.env")
Api = os.getenv("Quotes_API")

url = "https://api.api-ninjas.com/v2/randomquotes"
headers = {"X-Api-Key":Api}

response = requests.get(url, headers=headers)
raw = response.json()

whole_doc = raw[0]

quote_only = whole_doc["quote"]

print(quote_only)





