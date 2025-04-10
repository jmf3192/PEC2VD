
# ACT3 PEC2
# Visualización alternativa OHLC
# Fuente: Dataset 3.csv

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset 3.csv", sep=";")
df.columns = df.columns.str.replace('"', '').str.strip()

df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
df = df.sort_values("Date")

for col in ["Open", "High", "Low", "Price"]:
    df[col] = df[col].str.replace(".", "", regex=False).str.replace(",", ".", regex=False)
    df[col] = pd.to_numeric(df[col], errors="coerce")

df.rename(columns={"Price": "Close"}, inplace=True)

plt.figure(figsize=(14, 7))
plt.plot(df["Date"], df["Open"], label="Open", color="blue")
plt.plot(df["Date"], df["High"], label="High", color="green")
plt.plot(df["Date"], df["Low"], label="Low", color="red")
plt.plot(df["Date"], df["Close"], label="Close", color="orange")

plt.title("ACT3 PEC2 - Evolución OHLC (Gráfico de Líneas)")
plt.xlabel("Fecha")
plt.ylabel("Precio (€)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("OHLC.png")
