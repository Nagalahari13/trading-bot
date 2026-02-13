from bot.client import get_client

try:
    client = get_client()

    
    result = client.futures_ping()
    print("✅ Connected to Binance Testnet successfully!")

except Exception as e:
    print("❌ Connection failed:", str(e))
