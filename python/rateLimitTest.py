import requests
import time
import json
import datetime

API_KEY = 'ZGOSSLJVHHWNHLZ0'

API_KEY = 'ZGOSSLJVHHWNHLZ0'

symbols = ['AAPL','GOOGL','SSNLF','MSFT', 'NVDA','AMZN','PLTR','SPY','QQQ','JPM'] #list of stocks symbol

for symbol in symbols: #looping through my list of symbols stocks
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}' # make the api call for each symbols in the list

    print("Making API request...")
    print(f"URL: {url}")

    try:
        BeginTime = datetime.datetime.now() #Get the time at the beginning of the run
        response = requests.get(url)

        if response.status_code == 200:
            print("Success! API is working")

            data = response.json()

            print("\nAPI Response: ")
            print(json.dumps(data, indent = 2))

        else:
            print(f"Error: Status code {response.status_code}")
        StopTime = datetime.datetime.now() #Get the time at the end of the run
        API_Time = StopTime - BeginTime # Wait 8 seconds between requests to respect rate limits
        print(f'API call took: {API_Time.total_seconds():.3f} seconds')
        time.sleep(8) #Wait 8 seconds between requests to respect rate limits

    except Exception as e:
        print(f"Error: {e}")
    

