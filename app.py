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
    nvda_df = yf.download("^TNX",
                      start=d2,
                      end=d1,
                      progress=False)

    # View the first fiew records
    print(nvda_df)

def get_data():
    COMPANIES = ['NVDA', 'GME', '^TNX', '^IXIC']
    portforlio_cmp = {
                "GME":{"num_shares":10, "value":0.0, "weight":0.0, "weighted_beta":0.0},
                "NVDA":{"num_shares":5, "value":0.0, "weight":0.0, "weighted_beta":0.0}
                    }

    # Set Object
    yfs = YahooFinancials(COMPANIES)

    # Set date range
    today = date.today()
    dta = timedelta(days=2)
    prev = today - dta
    d1 = today.strftime("%Y-%m-%d")
    d2 = prev.strftime("%Y-%m-%d")

    # maket the call
    data = yfs.get_historical_price_data(start_date=d2, 
                                         end_date=d1, 
                                         time_interval='monthly')
    stats_data = yfs.get_key_statistics_data()

    total_asset_price = 0.0
    for stock in portforlio_cmp:
        portforlio_cmp[stock]["value"] = float(data[stock]['prices'][-1]['close']) * portforlio_cmp[stock]["num_shares"]
        total_asset_price += portforlio_cmp[stock]["value"]
    # update the weight
    portforlio_beta = 0.0
    for stock in portforlio_cmp:
        portforlio_cmp[stock]["weight"] = float(data[stock]['prices'][-1]['close']) * portforlio_cmp[stock]["num_shares"] / total_asset_price
        portforlio_cmp[stock]["weighted_beta"] = portforlio_cmp[stock]["weight"] * float(stats_data[stock]['beta'])
        portforlio_beta += portforlio_cmp[stock]["weighted_beta"]

        
    portfolio_expected_return = float(data['^TNX']['prices'][-1]['close'])/100 + portforlio_beta * (0.1 - float(data['^TNX']['prices'][-1]['close'])/100)
    print(portfolio_expected_return)
    

if __name__ == '__main__':
    # show_data()
    get_data()