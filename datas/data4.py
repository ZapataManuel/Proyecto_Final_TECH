import pandas as pd
import matplotlib.pyplot as plt


# Paso 1: Cargar el archivo CSV
df = pd.read_csv("powerplants.csv")

# Paso 2: Ver columnas reales (algunas tienen espacios o caracteres especiales)
df.columns = df.columns.str.strip()  # quitar espacios
print("Columnas:", df.columns.tolist())

# Paso 3: Eliminar filas completamente vacías
df.dropna(how='all', inplace=True)

# Paso 4: Limpiar campos clave
df["country_long"] = df["country_long"].astype(str).str.strip()
df["primary_fuel"] = df["primary_fuel"].astype(str).str.strip()

# Paso 5: Lista de países europeos (puedes ampliarla si necesitas más)
paises_europeos = [
    'Albania', 'Alemania', 'Andorra', 'Armenia', 'Austria', 'Bélgica', 'Bosnia and Herzegovina',
    'Bulgaria', 'Croacia', 'Chipre', 'Dinamarca', 'Eslovaquia', 'Eslovenia', 'España', 'Estonia',
    'Finlandia', 'Francia', 'Georgia', 'Grecia', 'Hungría', 'Irlanda', 'Islandia', 'Italia', 
    'Kosovo', 'Letonia', 'Liechtenstein', 'Lituania', 'Luxemburgo', 'Malta', 'Moldavia', 
    'Mónaco', 'Montenegro', 'Noruega', 'Países Bajos', 'Polonia', 'Portugal', 'Reino Unido',
    'República Checa', 'Rumania', 'San Marino', 'Serbia', 'Suecia', 'Suiza', 'Ucrania', 'Vaticano'
]

# Paso 6: Filtrar plantas hidroeléctricas en países europeos
df_filtrado = df[
    (df["primary_fuel"].str.lower() == "hydro") &
    (df["country_long"].isin(paises_europeos))
]

# Paso 7: Mostrar o guardar resultado
print(df_filtrado[["country_long", "name of powerplant", "capacity in MW", "primary_fuel"]])

# Guardar limpio (opcional)
df_filtrado.to_csv("plantas_hidroelectricas_europa.csv", index=False)



df=pd.read_csv('plantas_hidroelectricas_europa.csv')
df.to_json('energy.json',orient='records')



# Ruta al archivo CSV limpio
df = pd.read_csv("plantas_hidroelectricas_europa.csv")

# Limpieza básica
df.columns = df.columns.str.strip()
df["country_long"] = df["country_long"].astype(str).str.strip()
df["primary_fuel"] = df["primary_fuel"].astype(str).str.strip()

# Lista de países europeos
paises_europeos = [
    'Albania', 'Alemania', 'Andorra', 'Armenia', 'Austria', 'Bélgica', 'Bosnia and Herzegovina',
    'Bulgaria', 'Croacia', 'Chipre', 'Dinamarca', 'Eslovaquia', 'Eslovenia', 'España', 'Estonia',
    'Finlandia', 'Francia', 'Georgia', 'Grecia', 'Hungría', 'Irlanda', 'Islandia', 'Italia', 
    'Kosovo', 'Letonia', 'Liechtenstein', 'Lituania', 'Luxemburgo', 'Malta', 'Moldavia', 
    'Mónaco', 'Montenegro', 'Noruega', 'Países Bajos', 'Polonia', 'Portugal', 'Reino Unido',
    'República Checa', 'Rumania', 'San Marino', 'Serbia', 'Suecia', 'Suiza', 'Ucrania', 'Vaticano'
]

# Filtro: plantas hidroeléctricas en Europa
df_hydro = df[
    (df["primary_fuel"].str.lower() == "hydro") &
    (df["country_long"].isin(paises_europeos))
]

# Convertir capacidad a numérico
df_hydro["capacity in MW"] = pd.to_numeric(df_hydro["capacity in MW"], errors="coerce")
df_hydro.dropna(subset=["capacity in MW"], inplace=True)

# Agrupar por país y sumar capacidad
capacidad_por_pais = df_hydro.groupby("country_long")["capacity in MW"].sum()

# Graficar pie chart
plt.figure(figsize=(15, 15), palette="viridis")
capacidad_por_pais.plot(
    kind="pie", 
    autopct="%1.1f%%", 
    startangle=90,
    
)

plt.title("Distribución de energía hidroeléctrica en Europa (MW)")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Calcular porcentaje por país
porcentaje_por_pais = (capacidad_por_pais / capacidad_por_pais.sum()) * 100
porcentaje_por_pais = porcentaje_por_pais.round(1)
porcentaje_por_pais.to_json("hydro_europa.json", orient="index")
print("Archivo exportado: hydro_europa.json")
