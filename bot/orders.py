import logging

def place_market_order(client, symbol, side, quantity):
    logging.info(f"Placing MARKET order: {symbol} {side} {quantity}")
    
    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )
    
    logging.info(f"Response: {order}")
    return order


def place_limit_order(client, symbol, side, quantity, price):
    logging.info(f"Placing LIMIT order: {symbol} {side} {quantity} @ {price}")
    
    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )
    
    logging.info(f"Response: {order}")
    return order
