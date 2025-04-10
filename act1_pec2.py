
# ACT1 PEC2
# Gráfico de área con degradado: Exportaciones e Importaciones de España por País
# Fuente de los datos: dataset2.csv

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

df = pd.read_csv("dataset2.csv", sep=";")

merged_df = pd.concat([
    df[["Año", "País", "Exportaciones"]].rename(columns={"Exportaciones": "Valor"}).assign(Concepto="Exportaciones"),
    df[["Año", "País", "Importaciones"]].rename(columns={"Importaciones": "Valor"}).assign(Concepto="Importaciones")
])

merged_df["Año"] = pd.to_numeric(merged_df["Año"], errors="coerce")
merged_df["Valor"] = pd.to_numeric(merged_df["Valor"], errors="coerce")

merged_df = merged_df.dropna()

pivot = merged_df.pivot_table(index="Año", columns=["País", "Concepto"], values="Valor", aggfunc="sum")

cmap_china = get_cmap("Blues")
cmap_us = get_cmap("Greens")

plt.figure(figsize=(14, 8))
plt.stackplot(
    pivot.index,
    pivot["China", "Exportaciones"],
    pivot["China", "Importaciones"],
    pivot["Estados Unidos", "Exportaciones"],
    pivot["Estados Unidos", "Importaciones"],
    labels=[
        "Exportaciones - China",
        "Importaciones - China",
        "Exportaciones - Estados Unidos",
        "Importaciones - Estados Unidos"
    ],
    colors=[cmap_china(0.6), cmap_china(0.3), cmap_us(0.6), cmap_us(0.3)],
    alpha=0.8
)

plt.title("ACT1 PEC2 - Exportaciones e Importaciones de España por País (Degradado)")
plt.xlabel("Año")
plt.ylabel("Valor (€)")
plt.legend(loc="upper left")
plt.grid(True)
plt.tight_layout()

plt.savefig("exportaciones_importaciones_area.png")
