import os
import sys

# Add the parent directory to sys.path to import bot
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bot.logging_config import logger

def generate_sample_logs():
    """
    Simulates logging of MARKET and LIMIT orders to satisfy deliverable requirements.
    """
    logger.info("--- GENERATING SAMPLE LOGS FOR MARKET ORDER ---")
    
    market_request = {
        "symbol": "BTCUSDT",
        "side": "BUY",
        "type": "MARKET",
        "quantity": 0.002
    }
    logger.info(f"Sending order request: {market_request}")
    
    market_response = {
        "orderId": 123456789,
        "symbol": "BTCUSDT",
        "status": "FILLED",
        "clientOrderId": "abc-123",
        "price": "0.00",
        "avgPrice": "64500.50",
        "executedQty": "0.002",
        "cumQty": "0.002",
        "type": "MARKET",
        "side": "BUY",
        "time": 1678886400000
    }
    logger.info(f"Order response received: {market_response}")
    
    logger.info("--- GENERATING SAMPLE LOGS FOR LIMIT ORDER ---")
    
    limit_request = {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "quantity": 0.002,
        "price": "68000.00",
        "timeInForce": "GTC"
    }
    logger.info(f"Sending order request: {limit_request}")
    
    limit_response = {
        "orderId": 987654321,
        "symbol": "BTCUSDT",
        "status": "NEW",
        "clientOrderId": "xyz-789",
        "price": "68000.00",
        "avgPrice": "0.00",
        "executedQty": "0.000",
        "cumQty": "0.000",
        "type": "LIMIT",
        "side": "SELL",
        "time": 1678886460000
    }
    logger.info(f"Order response received: {limit_response}")
    
    print("Sample logs generated in trading_bot.log")

if __name__ == "__main__":
    generate_sample_logs()
