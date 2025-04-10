
# ACT2 PEC2
# Análisis de Correlación: Ausentismo Laboral
# Fuente del dataset: https://archive.ics.uci.edu/dataset/445/absenteeism+at+work

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv("Dataset 2.csv", sep=';')

# Seleccionar solo columnas numéricas
df_numeric = df.select_dtypes(include=["number"])

# Calcular la matriz de correlación
correlation_matrix = df_numeric.corr()

# Crear el mapa de calor de la matriz de correlación
plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True, cbar_kws={"shrink": .8})
plt.title("Matriz de Correlación - Dataset de Ausentismo Laboral")
plt.tight_layout()

# Guardar la figura
plt.savefig("matriz_correlacion.png")
