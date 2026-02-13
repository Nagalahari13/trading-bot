import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

def get_client():
    if not API_KEY or not API_SECRET:
        raise Exception("API keys not found in .env file")

    client = Client(
        API_KEY,
        API_SECRET,
        testnet=True  # THIS IS IMPORTANT
    )

    return client
