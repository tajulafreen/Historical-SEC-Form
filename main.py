from scripts.process_data import process_data
from scripts.stock_data import fetch_stock_data

def main():
    # Process the extracted data
    input_file = './data/raw_data/sec_fillings.csv'  # Path to the extracted data from Octoparse
    processed_file = './output/processed_data.csv'  # Path to save the processed data
    process_data(input_file, processed_file)

    # Fetch stock data
    stock_symbols = ['AAPL', 'GOOGL', 'AMZN']  # Example stock symbols
    stock_data_file = './output/stock_data.csv'  # Path to save stock data
    fetch_stock_data(stock_symbols, stock_data_file)

if __name__ == "__main__":
    main()
