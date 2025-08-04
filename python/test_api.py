import requests
import json

API_KEY = 'ZGOSSLJVHHWNHLZ0'

url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=AAPL&apikey={API_KEY}'

print("Making API request...")
print(f"URL: {url}")

try:
    response = requests.get(url)

    if response.status_code == 200:
        print("Success! API is working")

        data = response.json()

        print("\nAPI Response: ")
        print(json.dumps(data, indent = 2))

    else:
        print(f"Error: Status code {response.status_code}")

except Exception as e:
    print(f"Error: {e}")

