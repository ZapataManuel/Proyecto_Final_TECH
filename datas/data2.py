import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Cargar los datos
df = pd.read_csv("Continent_Consumption_TWH.csv")  

# Verificar nombres de columnas (por si hay espacios)
df.columns = df.columns.str.strip()


# 1. Exportar todos los años (para gráfico de línea)
linea_dict = dict(zip(df["Year"], df["Europe"]))
with open("europa_linea.json", "w") as f:
    json.dump(linea_dict, f)

# 2. Exportar desde el año 2000 (para gráfico de barras)
df_filtrado = df[df["Year"] >= 2000]
barras_dict = dict(zip(df_filtrado["Year"], df_filtrado["Europe"]))
with open("europa_barras.json", "w") as f:
    json.dump(barras_dict, f)

#1 Gráfico de línea para Europe
plt.figure(figsize=(10, 6))
sns.lineplot(
    data=df,
    x="Year",
    y="Europe",
    marker="o",
    color="green"
)
plt.title("Evolución de participación energética de Europa")
plt.xlabel("Año")
plt.ylabel("Valor (%) o cantidad")  
plt.grid(True)
plt.tight_layout()
plt.show()

#2 Gráfico de barras de Europa desde 2000

df_filtrado = df[df["Year"] >= 2000]
plt.figure(figsize=(10, 6))
sns.barplot(
    data=df_filtrado,
    x="Year",
    y="Europe",
    color="seagreen"
)
plt.title("Participación energética de Europa (2000 en adelante)")
plt.xlabel("Año")
plt.ylabel("Valor (%) o cantidad")  # Ajusta si es porcentaje
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



