

print("STOCKS REPORT...")



from app.utilities import to_usd
from app.alphavantage_service import fetch_stocks_data


symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"

df = fetch_stocks_data(symbol) 
print(df.columns)
#breakpoint()

latest = df.iloc[0]

print(symbol)
print(latest["timestamp"])
print(latest["close"])
print(to_usd(latest["close"]))
