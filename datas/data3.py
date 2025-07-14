import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# --- Países de Europa incluidos ---
paises_europa = [
    "Germany", "France", "Spain", "Italy", "United Kingdom", "Sweden", "Norway", "Finland",
    "Denmark", "Netherlands", "Belgium", "Austria", "Switzerland", "Portugal", "Ireland",
    "Poland", "Czech Republic", "Greece", "Hungary", "Romania", "Slovakia", "Slovenia",
    "Estonia", "Latvia", "Lithuania", "Bulgaria", "Croatia", "Serbia", "Ukraine"
]

# --- Cargar y limpiar datos ---
df = pd.read_csv("08 wind-generation_clean.csv")
df.columns = df.columns.str.strip()
df = df[df["Entity"].isin(paises_europa)]
df = df.dropna(subset=["Electricity from wind (TWh)", "Year"])
df["Year"] = df["Year"].astype(int)

# --- Filtrar desde el año 2000 ---
df_filtrado = df[df["Year"] >= 2000]

# --- Agrupar total por país desde 2000 (para top 10) ---
df_sumado = df_filtrado.groupby("Entity")["Electricity from wind (TWh)"].sum().sort_values(ascending=False)

# --- Tomar top 10 países para gráfico de barras ---
top10_sumado = df_sumado.head(10)



# --- Agrupación por año y país (para JSON y gráfico de área) ---
df_sum = df_filtrado.groupby(["Year", "Entity"])["Electricity from wind (TWh)"].sum().reset_index()

# --- Pivotear: filas = años, columnas = países ---
df_pivot = df_sum.pivot(index="Year", columns="Entity", values="Electricity from wind (TWh)").fillna(0)

# --- Exportar JSON en formato Chart.js (orient="columns") ---
df_pivot = df_pivot.round(2).astype(float)
df_pivot.to_json("europa_eolica.json", orient="columns")

# --- Exportar JSON como objeto {pais: total_twh} ---
top10_dict = top10_sumado.to_dict()

with open("top10_wind_generation.json", "w") as f:
    json.dump(top10_dict, f, indent=4)


# --- Gráfico de barras (Top 10) ---
plt.figure(figsize=(10, 6))
sns.barplot(
    x=top10_sumado.values,
    y=top10_sumado.index,
    palette="Blues_r"
)
plt.title("Top 10 países europeos en generación eólica (2000 en adelante)")
plt.xlabel("Total generado (TWh)")
plt.ylabel("País")
plt.tight_layout()
plt.show()



df_pivot.plot.area(figsize=(12, 6), cmap="viridis")
plt.title("Generación total de electricidad eólica en Europa por país (TWh)")
plt.xlabel("Año")
plt.ylabel("TWh")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()





