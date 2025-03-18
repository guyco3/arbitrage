import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()  # This assumes the .env file is in the current working directory

# Access the API_Key
COIN_GECKO_API_KEY = os.getenv('COIN_GECKO_API_KEY')

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": COIN_GECKO_API_KEY
}
response = requests.get(url, headers=headers)

print(response.text)