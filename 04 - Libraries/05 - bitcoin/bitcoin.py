import sys
import requests

bitcoin_price = 0
bitcoin_total = 0
try:
    user_price_request = sys.argv[1]
    user_price_request = float(user_price_request)
except IndexError:
    print("Missing command-line argument")
    sys.exit()
except ValueError:
    print("Command-line argument is not a number")
    sys.exit()
        

api_request = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=8b17fb4826cfc5f07c45a0c3265dd4e16d74abfca19848e0e4dd7bfb6e2d761b")

for key, value in api_request.items():
    if key == "priceUsd":
        bitcoin_price = value

bitcoin_total = bitcoin_price * user_price_request
print(f"{bitcoin_total:.4f}")
