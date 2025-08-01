import requests

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = response.json()

print("Bitcoin price in USD:", data['bpi']['USD']['rate'])