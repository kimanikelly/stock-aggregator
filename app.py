import click
from stock_class import Stock_Data

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


if __name__ == "__main__":
    while True:
        cli()
