import os
from binance.client import Client
from binance.exceptions import BinanceAPIException
from bot.logging_config import logger
from dotenv import load_dotenv

# Load environment variables from .env if it exists
load_dotenv()

class BinanceFuturesClient:
    """
    A wrapper around the Binance Futures Client for the Testnet.
    """
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")
        self.use_testnet = os.getenv("USE_TESTNET", "True").lower() == "true"
        self.client = None

    def connect(self):
        """
        Initializes the Binance Client.
        """
        if not self.api_key or not self.api_secret:
            logger.error("API Key or Secret missing. Please set BINANCE_API_KEY and BINANCE_API_SECRET in your .env file.")
            raise ValueError("API credentials missing.")

        try:
            # Initialize client for Futures
            self.client = Client(self.api_key, self.api_secret, testnet=self.use_testnet)
            
            # Explicitly set the testnet base URL if using testnet
            if self.use_testnet:
                self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi/v1'
                logger.info(f"Using Testnet Base URL: {self.client.FUTURES_URL}")
            
            logger.info(f"Connected to Binance {'Testnet' if self.use_testnet else 'Mainnet'} Futures.")
        except Exception as e:
            logger.error(f"Failed to connect to Binance API: {e}")
            raise

    def get_client(self):
        if not self.client:
            self.connect()
        return self.client
