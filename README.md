# Crypto Arbitrage Solver
This project aims to identify arbitrage opportunities using data from CoinGecko's API for data collection and the Bellman-Ford algorithm to detect negative cycles, which indicate potential arbitrage.

### Project Structure

- **arbitrage**: This directory serves as a module for the arbitrage solver.
  - **solver.py**: Contains the implementation of the Bellman-Ford algorithm to find negative cycles.
  - **tests**: Directory for unit tests to ensure the solver's correctness.
- **LICENSE**: Project licensing information.
- **README.md**: This file provides an overview of the project.

### Planned Additions

- **docs**: Documentation directory for detailed project explanations and usage guides.
- **examples**: Directory containing example usage scripts.
- **requirements.txt**: File listing all Python dependencies required to run the project.
- **setup.py**: Setup file for packaging and distributing the project.

### How It Works

#### Converting Exchange Rates to Edges

To apply the Bellman-Ford algorithm, we need to convert exchange rates into weighted edges in a graph. This is achieved by taking the logarithm of the exchange rates. Let $$ r_{ij} $$ be the exchange rate from currency $$ i $$ to currency $$ j $$, and let $$ f_{ij} $$ be the transaction fee associated with this exchange. The weight $$ w_{ij} $$ of the edge from $$ i $$ to $$ j $$ is calculated as follows:

$$ w_{ij} = -\log(r_{ij} \cdot (1 - f_{ij})) $$

This transformation ensures that a negative cycle in the graph corresponds to an arbitrage opportunity.

#### Bellman-Ford Algorithm

The Bellman-Ford algorithm is used to detect negative cycles in the graph. If a negative cycle exists, it means there is a sequence of trades that can yield a profit without risk.

### Contributing

Contributions are welcome! Please submit pull requests with clear explanations of changes.

### Running Tests

To run unit tests, navigate to the project directory and execute:
```bash
python -m unittest discover -s arbitrage/tests
```


### Future Development

- Enhance the solver to handle more complex arbitrage scenarios.
- Integrate additional APIs for broader market coverage.


