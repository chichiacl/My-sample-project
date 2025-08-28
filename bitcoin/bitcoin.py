import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

API = "MyApiKey"
URL = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API}"
try:
    response = requests.get(URL)
    response.raise_for_status()
    content = response.json()
    price = float(content["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("Error fetching data from CoinCap API")
except (KeyError, TypeError, ValueError):
    sys.exit("Error parsing data from CoinCap API")

total = bitcoins * price
print(f"${total:,.4f}")
