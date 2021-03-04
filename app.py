import click
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
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

def get_data():
    COMPANIES = ['NVDA', 'GME']

    # Set Object
    yfs = YahooFinancials(COMPANIES)

    # Set date range
    today = date.today()
    dta = timedelta(days=365)
    prev = today - dta
    d1 = today.strftime("%Y-%m-%d")
    d2 = prev.strftime("%Y-%m-%d")

    # maket the call
    data = yfs.get_historical_price_data(start_date=d2, 
                                                    end_date=d1, 
                                                    time_interval='monthly')
    print(data['NVDA']['prices'])

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    #show_data()
    get_data()