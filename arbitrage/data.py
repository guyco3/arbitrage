import requests
import os
import networkx as nx
# Load environment variables from .env

class CoinGeckoData:
    def __init__(self, coin_gecko_api_key):
        self.data = []
        self.graph = nx.DiGraph()  # Directed graph for exchange rates
        self._api_key = coin_gecko_api_key

    def fetch_data(self):
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
        # If you're using a demo API key, include it in headers
        if self._api_key:
            headers = {
                "accept": "application/json",
                "x-cg-demo-api-key": self._api_key
            }
        else:
            headers = {
                "accept": "application/json"
            }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            self.data = response.json()
            print("Data fetched successfully.")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    def convert_to_graph(self):
        # Assuming exchange rates are not directly available in the data,
        # we'll simulate adding edges based on hypothetical exchange rates.
        # In a real scenario, you'd need to fetch or calculate these rates.
        
        for coin in self.data:
            symbol = coin['symbol']
            self.graph.add_node(symbol)
            
            # For demonstration, let's assume we have exchange rates
            # and fees. In practice, you'd fetch these from another API or database.
            # Here, we're simulating exchange rates and fees for simplicity.
            for other_coin in self.data:
                if other_coin != coin:
                    other_symbol = other_coin['symbol']
                    # Simulated exchange rate and fee
                    exchange_rate = 1.0  # Replace with actual exchange rate
                    fee = 0.01  # Replace with actual transaction fee
                    
                    # Calculate weight as per your formula
                    weight = -1 * (exchange_rate * (1 - fee))
                    
                    self.graph.add_edge(symbol, other_symbol, weight=weight)

    def search_coin(self, symbol):
        for coin in self.data:
            if coin['symbol'] == symbol:
                return coin
        return None

# Example usage
if __name__ == "__main__":
    data_manager = CoinGeckoData()
    data_manager.fetch_data()
    data_manager.convert_to_graph()
    
    # Search for a specific coin
    coin_data = data_manager.search_coin('btc')
    if coin_data:
        print(coin_data)
    else:
        print("Coin not found.")
