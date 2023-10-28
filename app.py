import click
import time
from stock_class import Stock_Data
from database.db_connection import *

stock_data = Stock_Data()


@click.group()
def cli():
    pass


@cli.command("quote", help="Returns the current price of a stock ticker")
@click.option("--ticker", prompt='Stock Ticker')
def quote_endpont(ticker):

    if stock_data.quote(f"{ticker}") == 0:
        click.echo(click.style(ticker, fg='red') +
                   ": Is not a valid stock ticker")
    else:

        current_price = stock_data.quote(f"{ticker}")

        click.echo("The current price of " f"{ticker} is: " +
                   click.style(f"{'$'}{current_price}", fg='green'))

        sql = "INSERT INTO stock_prices (stock_ticker, current_price) VALUES (%s, %s)"
        val = (ticker, current_price)
        cursor.execute(sql, val)

        aggregator_db.commit()


if __name__ == "__main__":
    cli()
