import pandas as pd
import yfinance as yf

# Specify Dataframe and download past months figures
nvda_df = yf.download('NVDA',
                      start='2021-01-01',
                      end='2021-01-27',
                      progress=False)

# View the first fiew records
print(nvda_df.head())
