import requests
import sys

if len(sys.argv) <= 1:
    sys.exit("Missing command-line argument")

if not sys.argv[1].isnumeric():
    sys.exit("Command-line argument is not a number")


try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey")
    content = response.json()
    print(content)
except requests.RequestException:
    sys.exit()
