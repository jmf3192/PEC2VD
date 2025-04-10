
# ACT3 PEC2
# Visualización OHLC (Open-High-Low-Close) con datos financieros
# Fuente: Dataset 3.csv

import pandas as pd
import mplfinance as mpf

# Cargar el dataset
df = pd.read_csv("Dataset 3.csv", sep=";")

# Limpiar nombres de columnas
df.columns = df.columns.str.replace('"', '').str.strip()

# Convertir fecha y ordenarla
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
df = df.sort_values("Date")

# Reemplazar comas y convertir a float
for col in ["Open", "High", "Low", "Price"]:
    df[col] = df[col].str.replace(".", "", regex=False).str.replace(",", ".", regex=False)
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Renombrar columna "Price" a "Close" para mplfinance
df.rename(columns={"Price": "Close"}, inplace=True)

# Establecer índice temporal
df.set_index("Date", inplace=True)

# Seleccionar columnas para gráfico OHLC
df_ohlc = df[["Open", "High", "Low", "Close"]]

# Crear gráfico OHLC
mpf.plot(df_ohlc, type='ohlc', style='charles', title='ACT3 PEC2 - OHLC Chart',
         ylabel='Precio (€)', volume=False, figratio=(14,7), figscale=1.2,
         savefig='ACT3_PEC2_OHLC.png')
