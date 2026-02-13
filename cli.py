import argparse
import logging

from bot.client import get_client
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_side, validate_order_type, validate_quantity
from bot.logging_config import setup_logging

setup_logging()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    try:
        print("🔄 Processing order...")

        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)

        client = get_client()

        if args.type == "MARKET":
            order = place_market_order(
                client,
                args.symbol,
                args.side,
                args.quantity
            )
        else:
            if not args.price:
                raise ValueError("Price required for LIMIT order")

            order = place_limit_order(
                client,
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )
        print("\n✅ ORDER SUCCESS")
        print("Order ID:", order.get("orderId", "Not Available"))
        print("Status:", order.get("status", "Not Available"))
        print("Executed Qty:", order.get("executedQty", "Not Available"))
        print("Average Price:",order.get("avgPrice"))
        print("Full Response:", order)


    except Exception as e:
        logging.error(str(e))
        print("\n ERROR:", str(e))


if __name__ == "__main__":
    main()
