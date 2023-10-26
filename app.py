import click
from api.finnhub import Stock_Data

stock_data = Stock_Data()

@click.group()
def cli():
    pass
    
@cli.command("quote", help="Testing")
@click.argument("symbol")
def quote_endpont(symbol):

    click.echo(stock_data.quote(symbol))
 
if __name__ == "__main__":
    cli()