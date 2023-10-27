import click
from finnhub_class import Stock_Data

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
        result = stock_data.quote(f"{ticker}")
        click.echo(click.style(f"{'$'}{result}", fg='green'))


if __name__ == "__main__":
    cli()
