import yfinance as yf
import datetime

while(1):
    #Accept symbol as input from user
    print("Please enter a symbol:") 
    print()
    StockSymbol = input()
    print()

    try:
        stock = yf.Ticker(StockSymbol)
    except ConnectionError as e:
        print("Connection error", e)
        break
    dt = datetime.datetime.now() 
    dateTimeValue = dt.strftime("%c") 
    print(dateTimeValue)
    print()
    if(stock.info['regularMarketPrice'] is None):
        print("Invalid symbol")
    else:
        print(stock.info['longName'],"(",StockSymbol,")")
        print()

        current_stock_price = stock.info['currentPrice']
        previous_day_stock_price = stock.info['previousClose']
        price_difference = current_stock_price - previous_day_stock_price
        
        percent_difference = abs(price_difference/previous_day_stock_price)*100

        percent_difference = "{0:.2f}".format(percent_difference)
        if(price_difference > 0):
            print(current_stock_price,"+",price_difference,"(+",percent_difference,"%",")")
        else:
            print(current_stock_price,"-",abs(price_difference),"(-",percent_difference,"%",")")

    print("-------------------------------------------------------------------------")
    print()
    print()  



