import sys
import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from bot.logging_config import logger
from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.validators import (
    validate_symbol, validate_side, validate_order_type, 
    validate_quantity, validate_price
)

console = Console()

@click.command()
@click.option('--symbol', required=True, help='Trading symbol (e.g., BTCUSDT)')
@click.option('--side', required=True, type=click.Choice(['BUY', 'SELL'], case_sensitive=False), help='Order side')
@click.option('--type', 'order_type', required=True, type=click.Choice(['MARKET', 'LIMIT'], case_sensitive=False), help='Order type')
@click.option('--quantity', required=True, help='Quantity to trade')
@click.option('--price', help='Price (required for LIMIT orders)')
def place_order(symbol, side, order_type, quantity, price):
    """
    Binance Futures Trading Bot CLI
    """
    try:
        # Validate inputs
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)

        # Print request summary
        request_table = Table(title="Order Request Summary", show_header=True, header_style="bold magenta")
        request_table.add_column("Property", style="dim")
        request_table.add_column("Value")
        request_table.add_row("Symbol", symbol)
        request_table.add_row("Side", side)
        request_table.add_row("Type", order_type)
        request_table.add_row("Quantity", str(quantity))
        if price:
            request_table.add_row("Price", str(price))
        
        console.print(request_table)

        # Initialize Client and Order Manager
        bot_client = BinanceFuturesClient()
        client = bot_client.get_client()
        order_manager = OrderManager(client)

        # Place Order
        response = order_manager.place_order(symbol, side, order_type, quantity, price)

        # Print success response details
        response_table = Table(title="Order Execution Details", show_header=True, header_style="bold green")
        response_table.add_column("Field")
        response_table.add_column("Value")
        response_table.add_row("OrderID", str(response.get('orderId')))
        response_table.add_row("Status", str(response.get('status')))
        response_table.add_row("Executed Qty", str(response.get('executedQty')))
        response_table.add_row("Avg Price", str(response.get('avgPrice', 'N/A')))
        
        console.print(Panel("✅ [bold green]Order Placed Successfully![/bold green]"))
        console.print(response_table)

    except ValueError as e:
        console.print(f"[bold red]Validation Error:[/bold red] {e}")
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)

if __name__ == "__main__":
    place_order()
