
# maybe something like the following rough organizational structure would be reasonable.
# then we can import these functions into other files that need them (i.e. crypto.py, stocks.py, unemployment.py).
# one benefit of doing so is we get to refactor all the request-related code out of those files.
# for example, as a result, we'll only have the api key definition in one place (which is good)!

import os
from dotenv import load_dotenv
from app.utilities import to_usd
from pandas import read_csv
import requests
import json

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")


def fetch_crypto_data(symbol):
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    tsd = parsed_response["Time Series (Digital Currency Daily)"]

    dates = list(tsd.keys())
    latest_date = dates[0]
    latest = tsd[latest_date]
        # #print(latest)
        # # not sure about the difference between '4a. close (USD)' and '4b. close (USD)'

    print(symbol)
    print(latest_date)
    print(latest['4a. close (USD)'])
    print(to_usd(float(latest['4a. close (USD)'])))
    


def fetch_stocks_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"

    df = read_csv(url)
    #latest = df.iloc[0]
    return df


def fetch_unemployment_data():
    url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text) 
    data = parsed_response["data"]
    latest = data[0]
    print(latest) #> {'date': '2022-02-01', 'value': '3.8'}
    from pandas import DataFrame
    from plotly.express import bar


    df = DataFrame(data)
    print(df.head())

    fig = bar(df, x="date", y="value", title="Unemployment Rates")
    # https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html

    # https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_yaxes
    # https://plotly.com/python/reference/layout/yaxis/
    # https://plotly.com/python/reference/layout/yaxis/#layout-yaxis-ticksuffix
    fig.update_yaxes(
        #tickprefix="$",
        ticksuffix="%",
        showgrid=True
    )

    fig.show()

    #breakpoint()


    print("DATAVIZ EXPORT...")
     # https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.to_image
    # fig.to_image(format="png")

    # https://plotly.com/python/static-image-export/
    # Image export using the "kaleido" engine requires the kaleido package,
    #which can be installed using pip:
    #    $ pip install -U kaleido
    img_filepath = os.path.join(os.path.dirname(__file__), "..", "reports", "unemployment.png")
    fig.write_image(img_filepath)


    print("CSV EXPORT...")
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "reports", "unemployment.csv")
    df.to_csv(csv_filepath, index=False)