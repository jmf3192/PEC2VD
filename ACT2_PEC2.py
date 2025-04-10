
# ACT2 PEC2
# Análisis de Correlación: Ausentismo Laboral
# Fuente del dataset: https://archive.ics.uci.edu/dataset/445/absenteeism+at+work

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Dataset2.csv", sep=';')

df_numeric = df.select_dtypes(include=["number"])

correlation_matrix = df_numeric.corr()

plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True, cbar_kws={"shrink": .8})
plt.title("Matriz de Correlación - Dataset de Ausentismo Laboral")
plt.tight_layout()

plt.savefig("matriz_correlacion.png")
