
# ACT3 PEC2
# Visualización OHLC
!pip install mplfinance

import pandas as pd
import mplfinance as mpf
from google.colab import files
import io


df = pd.read_csv('Dataset 3.csv', sep=";")

df.columns = df.columns.str.replace('"', '').str.strip()

df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
df = df.sort_values("Date")

for col in ["Open", "High", "Low", "Price"]:
    df[col] = df[col].str.replace(".", "", regex=False).str.replace(",", ".", regex=False)
    df[col] = pd.to_numeric(df[col], errors="coerce")

df.rename(columns={"Price": "Close"}, inplace=True)

df.set_index("Date", inplace=True)

df_ohlc = df[["Open", "High", "Low", "Close"]]

mpf.plot(df_ohlc, type='ohlc', style='charles',
         title='ACT3 PEC2 - OHLC Chart',
         ylabel='Precio (€)', volume=False,
         figratio=(14, 7), figscale=1.2)

