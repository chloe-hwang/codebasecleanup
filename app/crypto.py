


print("CRYPTO REPORT...")



from app.utilities import to_usd
from app.alphavantage_service import fetch_crypto_data



symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"

fetch_crypto_data(symbol)