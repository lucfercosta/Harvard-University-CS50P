import sys
import requests


try:
    user_price_request = float(sys.argv[1])
except IndexError:
    print("Missing command-line argument")
    sys.exit()
except ValueError:
    print("Command-line argument is not a number")
    sys.exit()
        

# Get request
api_request = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=8b17fb4826cfc5f07c45a0c3265dd4e16d74abfca19848e0e4dd7bfb6e2d761b")
# Convert request into json
data = api_request.json()
# Get priceUsd from json
bitcoin_price = float(data["data"]["priceUsd"])
# Get total price
bitcoin_total = bitcoin_price * user_price_request
# Print
print(f"{bitcoin_total:.4f}")
