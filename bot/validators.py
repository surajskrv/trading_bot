import re

def validate_symbol(symbol: str):
    """
    Validates Binance symbol format (e.g., BTCUSDT).
    """
    if not re.match(r"^[A-Z0-9]{5,15}$", symbol):
        raise ValueError(f"Invalid symbol format: {symbol}. Expected format like 'BTCUSDT'.")
    return symbol.upper()

def validate_side(side: str):
    """
    Validates order side (BUY or SELL).
    """
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError(f"Invalid side: {side}. Must be 'BUY' or 'SELL'.")
    return side

def validate_order_type(order_type: str):
    """
    Validates order type (MARKET or LIMIT).
    """
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError(f"Invalid order type: {order_type}. Must be 'MARKET' or 'LIMIT'.")
    return order_type

def validate_quantity(quantity: str):
    """
    Validates quantity is a positive number.
    """
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError
        return qty
    except ValueError:
        raise ValueError(f"Invalid quantity: {quantity}. Must be a positive number.")

def validate_price(price: str, order_type: str):
    """
    Validates price is a positive number (required for LIMIT orders).
    """
    if order_type.upper() == "LIMIT":
        if not price:
            raise ValueError("Price is required for LIMIT orders.")
        try:
            p = float(price)
            if p <= 0:
                raise ValueError
            return p
        except ValueError:
            raise ValueError(f"Invalid price: {price}. Must be a positive number.")
    return None
