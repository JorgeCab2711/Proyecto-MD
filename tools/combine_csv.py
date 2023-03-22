import os
import pandas as pd

# crear una lista de todos los archivos CSV en el directorio actual
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

# leer cada archivo CSV en un dataframe de Pandas y agregar una columna "año_info"
dfs = []
for file in csv_files:
    year = file.split()[1]  # obtener el año del nombre del archivo
    df = pd.read_csv(file)
    df['año_info'] = year.replace('.csv', '')
    dfs.append(df)

# combinar todos los dataframes en uno solo
combined_df = pd.concat(dfs, ignore_index=True)

# escribir el dataframe combinado en un nuevo archivo CSV
combined_df.to_csv('defunciones_combinadas.csv', index=False)


# verificar que la suma total de los elementos en cada archivo es igual a la cantidad de elementos en el archivo generado
total_rows = 0
for file in csv_files:
    df = pd.read_csv(file)
    # obtener la cantidad de filas en cada archivo y sumarlas
    total_rows += df.shape[0]
if total_rows == combined_df.shape[0]:
    print("La suma total de los elementos en cada archivo es igual a la cantidad de elementos en el archivo generado")
else:
    print("La suma total de los elementos en cada archivo NO es igual a la cantidad de elementos en el archivo generado")
