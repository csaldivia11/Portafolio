
# pipeline_original.py

import pandas as pd
import sqlite3

# Leer CSV
df_ventas = pd.read_csv('clientes_ventas.csv')
df_marketing = pd.read_csv('clientes_marketing.csv')
df_soporte = pd.read_csv('clientes_soporte.csv')

# Leer Excel
df_extra = pd.read_excel('clientes_extra.xlsx', sheet_name='Sheet1')

# Leer desde SQL
conn = sqlite3.connect('clientes_db.sqlite')
df_db = pd.read_sql('SELECT * FROM clientes_db', conn)

# Unir todo
df = pd.concat([df_ventas, df_marketing, df_soporte, df_extra, df_db])

# Eliminar duplicados
df = df.drop_duplicates()

# Limpieza mínima de nulos
df = df.dropna()

# Normalizar nombre de ciudades
df['ciudad'] = df['ciudad'].replace({'Sntiago': 'Santiago', 'Vina del Mr': 'Viña del Mar'})

# Guardar resultado
df.to_csv('clientes_unificados.csv', index=False)
