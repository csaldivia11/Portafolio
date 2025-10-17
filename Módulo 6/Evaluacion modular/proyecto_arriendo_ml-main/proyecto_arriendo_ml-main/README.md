# 🏘️ API de Predicción de Arriendo en Chile

Este proyecto demuestra cómo entrenar un modelo de machine learning en tiempo real con Python y Scikit-learn, y cómo desplegarlo como una API REST utilizando **FastAPI**. La aplicación predice el precio estimado de arriendo de una propiedad en distintas comunas de Chile, simulando un flujo real de ciencia de datos aplicada.

---

## 🎯 Enfoque del proyecto

Este proyecto NO utiliza modelos preentrenados ni archivos `.pkl`.  
El modelo se entrena directamente al iniciar la API.

Además, se incluye un notebook en Google Colab como recurso adicional para explorar y experimentar con el entrenamiento del modelo.

---

## 📁 Estructura del proyecto

```
proyecto_arriendo_ml/
├── app/
│   └── main.py                      ← Código de la API con entrenamiento integrado
├── data/
├── notebooks/
│   └── entrenamiento_modelo_colab.ipynb  
├── requirements.txt
├── .gitignore
├── README.md
```

---

## ✅ Pasos para ejecutar el proyecto

### 1. Descargar y descomprimir

Descarga el archivo `proyecto_arriendo_ml.zip` y descomprímelo en tu máquina.

---

### 2. Crear entorno virtual

```bash
python -m venv amb_proyecto_arriendo_ml
```

Activación:

- **Windows:** `amb_proyecto_arriendo_ml\Scripts\activate`
- **macOS/Linux:** `source amb_proyecto_arriendo_ml/bin/activate`

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Ejecutar la API local

```bash
uvicorn app.main:app --reload
```

Luego, abre en tu navegador:

```
http://localhost:8000/docs
```

Allí verás la documentación interactiva (Swagger) para probar el endpoint `/predecir`.

---

## 🧠 ¿Qué hace el archivo `main.py`?

El archivo `main.py` contiene una función llamada `entrenar_modelo()` que:

- Genera un dataset simulado con 300 registros
- Entrena un modelo de regresión lineal con Scikit-learn
- Expone el modelo como una API REST

Esto garantiza compatibilidad con tu entorno sin depender de versiones anteriores ni archivos externos.

---

## 📊 Ejemplo de uso en Swagger

Prueba el endpoint con el siguiente JSON:

```json
{
  "comuna": "Maipú",
  "tipo": "Departamento",
  "superficie": 60,
  "habitaciones": 2,
  "baños": 1
}
```

Y obtendrás una predicción como:

```json
{
  "precio_estimado": 645312
}
```

---

## 📘 Recurso adicional (Colab)

Si deseas entrenar el modelo de forma manual, visualizar datos o modificar la lógica, puedes usar el notebook incluido en:

```
notebooks/entrenamiento_modelo_colab.ipynb
```

Ideal para reforzar el aprendizaje antes de implementar en producción.

---

## 📚 Herramientas utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Scikit-learn](https://scikit-learn.org/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pandas](https://pandas.pydata.org/)
- [Google Colab](https://colab.research.google.com/)

---

## ✅ Buenas prácticas aplicadas

✔️ Entrenamiento reproducible  
✔️ API bien estructurada y documentada  
✔️ Flujo de desarrollo local + exploración en Colab  
✔️ Compatible con cualquier versión de entorno

---

## ✨ Reflexión final

Este proyecto representa una simulación realista del ciclo de vida de un modelo de machine learning. Desde la exploración y entrenamiento, hasta el despliegue y exposición vía API REST, permite entender cómo llevar soluciones de datos desde la teoría a la práctica.
