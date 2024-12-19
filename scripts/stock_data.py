import yfinance as yf
import pandas as pd

def fetch_stock_data(stock_symbols: list, output_file: str):
    stock_data = []

    for symbol in stock_symbols:
        # Fetch stock data
        stock = yf.Ticker(symbol)
        info = stock.history(period='1d')  # Get stock price for today
        stock_info = {
            'Symbol': symbol,
            'Stock Name': stock.info.get('shortName', 'N/A'),
            'Price': info['Close'].iloc[0],  # Corrected to avoid the FutureWarning
            'Market Cap': stock.info.get('marketCap', 'N/A')
        }
        stock_data.append(stock_info)

    # Convert data to DataFrame
    df = pd.DataFrame(stock_data)

    # Save to CSV
    df.to_csv(output_file, index=False)
    print(f"Stock data has been fetched and saved to {output_file}")
