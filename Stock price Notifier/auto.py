import yfinance as yf
from plyer import notification
import time

STOCK_SYMBOL = "AAPL"  # Replace with your chosen stock symbol
TARGET_PRICE = 150.00  # Set your target price

def check_stock_price():
    stock = yf.Ticker(STOCK_SYMBOL)
    current_price = stock.history(period="1d")["Close"].iloc[-1]
    return current_price

def send_notification(price):
    message = f"{STOCK_SYMBOL} has reached ${price:.2f}"
    notification.notify(
        title="Stock Price Alert",
        message=message,
        timeout=10
    )

def main():
    while True:
        price = check_stock_price()
        print(f"Current price of {STOCK_SYMBOL}: ${price:.2f}")
        
        if price >= TARGET_PRICE:
            send_notification(price)
            print("Notification sent!")
            break 
        time.sleep(1800)

if __name__ == "__main__":
    main()
