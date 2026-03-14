# Binance Futures Trading Bot (Testnet)

A simplified Python 3.x application to place **MARKET** and **LIMIT** orders on the **Binance Futures Testnet (USDT-M)**.

## Features
- ✅ Place **Market** and **Limit** orders.
- ✅ Support **BUY** and **SELL** sides.
- ✅ Input validation for symbol, quantity, price, and side.
- ✅ Structured logging to `trading_bot.log`.
- ✅ Premium CLI experience with `rich` formatting.
- ✅ Robust error handling for API and network issues.

## Prerequisites
- Python 3.8 or higher.
- A Binance Futures Testnet account (and API keys).

## Installation

1. **Clone or Download** the project to your local machine.
2. **Navigate** to the project directory:
   ```bash
   cd trading_bot
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Create a `.env` file** in the root `trading_bot` directory:
   ```bash
   cp .env.example .env
   ```
2. **Open `.env`** and add your Binance Testnet API credentials:
   ```env
   BINANCE_API_KEY=your_testnet_api_key
   BINANCE_API_SECRET=your_testnet_secret
   ```

## Usage

You can run the bot using the `cli.py` entry point. Use `--help` to see all available options:
```bash
python cli.py --help
```

### 1. Place a MARKET Order
Place a market buy order for **0.002 BTC** (to ensure it meets the $100 minimum notional requirement):
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### 2. Place a LIMIT Order
Place a limit sell order for **0.002 BTC** at $68,000:
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 68000
```

## Troubleshooting

### "Order's notional must be no smaller than 100"
Binance requires the **Notional Value** (`Price * Quantity`) of an order to be at least **100 USDT**. 
- **Fix**: Increase the `--quantity` or choose a more expensive price for LIMIT orders. 
- For example, at a BTC price of $65,000, a quantity of **0.001** is only $65 (too small), but **0.002** is $130 (valid).

## Project Structure
```text
trading_bot/
├── bot/
│   ├── client.py        # Binance API client wrapper
│   ├── orders.py        # Order placement logic
│   ├── validators.py    # Input validation functions
│   └── logging_config.py # Structured logging setup
├── scripts/
│   └── generate_sample_logs.py # Utility to generate required log deliverables
├── cli.py               # Main CLI entry point
├── trading_bot.log      # Auto-generated log file
├── requirements.txt     # Python dependencies
└── README.md            # You are here
```

## Assumptions
- The bot is hardcoded to use the **Binance Futures Testnet** URL: `https://testnet.binancefuture.com/fapi/v1`.
- `TimeInForce` for LIMIT orders defaults to `GTC` (Good 'Til Cancelled).
- Use `USDT` pairs (e.g., `BTCUSDT`, `ETHUSDT`).
