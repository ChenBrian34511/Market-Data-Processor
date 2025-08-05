import requests
import datetime
import csv

    
def validatePrice(price):
    prices = float(price)
    if (prices < 0): # checks if price is negative
        print(('something is wrong'))
        return False
    
    if (prices == 0): #checks if price equal to zero
        print ('company maybe bankrupt')
        return False

    if (prices < 1 or prices > 1000): #checks if price is in the range of 1-1000
        print('Price maybe too high')
        return False
    return True #If Everything is correct return True
def fetch_stock_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    
    try:
        response = requests.get(url) #Gets the HTTP response
        data = response.json() #contents converted to python dictionary
        if ("Error Message" in data): #API error
            print(f"API error for {symbol}") 
        
        elif ("Note" in data): #API Daily limit rate
            print("Rate limited! Waiting")
        
        else:
            price = data["Global Quote"]["05. price"] #Extract current stock price from successful API response
            TimeStamp = datetime.datetime.now()
            if validatePrice(price): #Check if extracted price is valid for use
                print(f"{symbol}: ${price} - Valid price") #Price passed validation - safe to use this data
                with open ('data/stock_data.csv', 'a') as data:
                    csvWriter = csv.writer(data)
                    csvWriter.writerow([symbol, price,TimeStamp])

            else:
                print(f"{symbol}: Skipping invalid price ${price}") #Print symbol but skip the price since its not correct

    except requests.exceptions.ConnectionError: #See if there is a problem with internet connection
        print("Internet connection problem")