# Binance Futures Trading Bot (Testnet)

A simple Python-based CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.


# Features

- Place MARKET orders (BUY / SELL)
- Place LIMIT orders (BUY / SELL)
- CLI-based input using argparse
- Input validation
- Logging of API requests and responses
- Error handling for invalid inputs and API failures
- Structured project architecture



# Project Structure

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
└── trading_bot.log



# Setup Instructions

# Clone the repository

git clone https://github.com/Nagalahari13/trading-bot.git
cd trading-bot


# Create virtual environment 

Windows:
python -m venv venv
venv\Scripts\activate


# Install dependencies

pip install -r requirements.txt


# Create .env file

Create a file named `.env` in the root directory and add:

API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret_key

You can generate API keys from Binance Futures Testnet:
https://testnet.binancefuture.com



# How to Run

# MARKET Order Example

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002


# LIMIT Order Example

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 20000




#  Output

On success, the program displays:

- Order ID
- Order Status
- Executed Quantity
- Average Price
- Full API Response

All API requests and responses are also logged in:

trading_bot.log



#  Assumptions

- This bot works only on Binance Futures Testnet.
- Minimum notional value required by Binance Futures is 100 USDT.
- Quantity must satisfy: price × quantity ≥ 100 USDT.
- .env file is not included in the repository for security reasons.
- MARKET orders on testnet may remain in "NEW" status due to testnet liquidity behavior.
- Only MARKET and LIMIT orders are implemented.



# Error Handling

The bot handles:

- Invalid order side
- Invalid order type
- Invalid quantity
- Missing price for LIMIT order
- Binance API errors
- Network issues

Errors are logged to `trading_bot.log`.



# Dependencies

- python-binance
- python-dotenv



# Author

Developed as part of Python Developer Intern Assignment.

