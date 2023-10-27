import click
from api.finnhub import Stock_Data

stock_data = Stock_Data()

@click.group()
def cli():
    pass
    
@cli.command("quote", help="Returns the current price of a stock ticker")
@click.option("--ticker", prompt='Stock Ticker')
def quote_endpont(ticker):

    if stock_data.quote(f"{ticker}") == 0:
        click.echo(f"{ticker}: Is not a valid stock ticker")
    else:
        click.echo(stock_data.quote(f"{ticker}"))
    

 
if __name__ == "__main__":
    cli()