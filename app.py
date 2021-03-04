import click
import pandas as pd
import yfinance as yf
from datetime import date, timedelta

@click.command()
@click.option('--name', prompt='Enter Stock Name',
              help='The stock you want to check.')

def show_data(name):
    today = date.today()
    dta = timedelta(days=30)
    prev = today - dta
    d1 = today.strftime("%Y-%m-%d")
    d2 = prev.strftime("%Y-%m-%d") 
    # Specify Dataframe and download past months figures
    nvda_df = yf.download(name,
                      start=d2,
                      end=d1,
                      progress=False)

# View the first fiew records
    print(nvda_df)

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    show_data()
