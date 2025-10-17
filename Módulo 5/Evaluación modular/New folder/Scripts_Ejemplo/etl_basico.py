import pandas as pd
import sqlite3

df = pd.read_csv("ventas.csv")
conn = sqlite3.connect("modelo_dw.sqlite")
df.to_sql("ventas", conn, if_exists="replace", index=False)
conn.close()