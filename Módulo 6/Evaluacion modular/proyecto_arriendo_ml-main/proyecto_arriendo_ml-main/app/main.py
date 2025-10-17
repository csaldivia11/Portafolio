from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

def entrenar_modelo_desde_csv():
    df = pd.read_csv("data/arriendos_chile_simulado.csv")

    X = df.drop("precio", axis=1)
    y = df["precio"]

    preprocessor = ColumnTransformer([
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['comuna', 'tipo'])
    ], remainder='passthrough')

    pipeline = Pipeline([
        ('preprocess', preprocessor),
        ('model', LinearRegression())
    ])

    pipeline.fit(X, y)
    return pipeline

modelo = entrenar_modelo_desde_csv()

app = FastAPI(title="API de Predicción de Arriendo (desde CSV)")

class DatosArriendo(BaseModel):
    comuna: str
    tipo: str
    superficie: int
    habitaciones: int
    baños: int

@app.post("/predecir")
def predecir(data: DatosArriendo):
    entrada = pd.DataFrame([{
        "comuna": data.comuna,
        "tipo": data.tipo,
        "superficie": data.superficie,
        "habitaciones": data.habitaciones,
        "baños": data.baños
    }])
    pred = modelo.predict(entrada)
    return {"precio_estimado": round(pred[0])}
