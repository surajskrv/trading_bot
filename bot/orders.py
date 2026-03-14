from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException
from bot.logging_config import logger

class OrderManager:
    """
    Handles placing Market and Limit orders on Binance Futures.
    """
    def __init__(self, binance_client):
        self.client = binance_client

    def place_order(self, symbol, side, order_type, quantity, price=None):
        """
        Places an order on Binance Futures Testnet.
        """
        try:
            params = {
                "symbol": symbol,
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": quantity
            }

            if order_type.upper() == "LIMIT":
                params["price"] = str(price)
                params["timeInForce"] = TIME_IN_FORCE_GTC  # Good 'Til Cancelled
            
            logger.info(f"Sending order request: {params}")
            
            # Use futures_create_order for USDT-M Futures
            response = self.client.futures_create_order(**params)
            
            logger.info(f"Order response received: {response}")
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.status_code} - {e.message}")
            raise
        except BinanceOrderException as e:
            logger.error(f"Binance Order Error: {e.message}")
            raise
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            raise
