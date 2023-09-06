from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://postgres@localhost:5432/etf')
df = pd.read_csv('ETF_prices.csv')
df.to_sql('daily', con=engine, if_exists='replace')
print(df.head())