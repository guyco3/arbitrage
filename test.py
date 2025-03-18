import requests
from dotenv import load_dotenv
import os
from arbitrage import CoinGeckoData
# Load environment variables from .env
load_dotenv()  # This assumes the .env file is in the current working directory

# Access the API_Key
COIN_GECKO_API_KEY = os.getenv('COIN_GECKO_API_KEY')


data = CoinGeckoData(COIN_GECKO_API_KEY)
data.fetch_data()

print(data.data[0])