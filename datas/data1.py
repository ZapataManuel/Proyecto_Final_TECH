import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# 1. Cargar los datos
df = pd.read_csv("14 solar-share-energy_Clean (1).csv")  

# 2. Limpiar datos (eliminar NaNs y datos incompletos)
df = df.dropna(subset=["Solar (% equivalent primary energy)", "Entity", "Year"])
df["Year"] = df["Year"].astype(int)

# 3. Filtrar solo países europeos
paises_europa = [
    "Germany", "France", "Spain", "Italy", "United Kingdom", "Sweden", "Norway", "Finland",
    "Denmark", "Netherlands", "Belgium", "Austria", "Switzerland", "Portugal", "Ireland",
    "Poland", "Czech Republic", "Greece", "Hungary", "Romania", "Slovakia", "Slovenia",
    "Estonia", "Latvia", "Lithuania", "Bulgaria", "Croatia", "Serbia", "Ukraine"
]

df = df[df["Entity"].isin(paises_europa)]

# 4. Filtrar el año más reciente
ultimo_anio = df["Year"].max()
df_ultimo = df[df["Year"] == ultimo_anio]

# 5. Obtener el top 15 de países europeos con mayor % solar
top15 = df_ultimo.sort_values(by="Solar (% equivalent primary energy)", ascending=False).head(15)

# Exportar Top 15 actual
top15_dict = dict(zip(top15["Entity"], top15["Solar (% equivalent primary energy)"]))
with open("top15_solar.json", "w") as f:
    json.dump(top15_dict, f)

# 6. Gráfico de barras horizontales - Top 15 europeos
plt.figure(figsize=(10, 6))
sns.barplot(
    data=top15,
    y="Entity",
    x="Solar (% equivalent primary energy)",
    palette="viridis"
)
plt.title(f"Top 15 países europeos con mayor % de energía solar hasta el año {ultimo_anio}")
plt.xlabel("% Energía solar (sobre energía primaria)")
plt.ylabel("País")
plt.tight_layout()
plt.show()

# 7. Filtrar el DataFrame original por los países top 15
paises_top15 = top15["Entity"].unique()
df_top15 = df[df["Entity"].isin(paises_top15)]



# 8. Promedio histórico de % solar en los países top 15 de Europa
df_promedios = df_top15.groupby("Entity")["Solar (% equivalent primary energy)"].mean().sort_values(ascending=False)

# Exportar correctamente
promedios_dict = df_promedios.to_dict()
with open("promedio_solar.json", "w") as f:
    json.dump(promedios_dict, f)


#grafico 

plt.figure(figsize=(10, 6))
sns.barplot(
    x=df_promedios.values,
    y=df_promedios.index,
    palette="crest"
)
plt.title("Promedio histórico del % de energía solar en países europeos ")
plt.xlabel("% Promedio de Energía Solar")
plt.ylabel("País")
plt.tight_layout()
plt.show()
