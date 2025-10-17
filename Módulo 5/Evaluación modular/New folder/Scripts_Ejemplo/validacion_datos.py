import pandas as pd

df = pd.read_csv("clientes.csv")
print("Registros duplicados:", df.duplicated().sum())
print("Valores nulos por columna:\n", df.isnull().sum())