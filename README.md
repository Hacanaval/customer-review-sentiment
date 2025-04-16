# Sentiment Analysis API
(Español al final)

This is a simple REST API built with Flask for analyzing customer reviews using two models: **VADER** and **TextBlob**. The API receives a text and the model to use, and returns the polarity score and sentiment classification.

---

## 📌 Features

- Supports two sentiment analysis models: **VADER** and **TextBlob**
- Returns compound polarity score and sentiment classification (Positive, Negative, Neutral)
- Easily extendable for integration with Firebase, frontend apps or batch processing

---

## 🚀 How to Use

### 1. Clone and Install
```bash
git clone https://github.com/your-user/sentiment-analysis-api.git
cd sentiment-analysis-api
pip install -r requirements.txt
```

### 2. Run the API locally
```bash
cd src
python app.py
```

### 3. Send a POST request to `/sentiment`
Use Postman, curl, or fetch:
```json
{
  "text": "This product is amazing!",
  "model": "vader"
}
```

**Valid models:** `vader`, `textblob`

**Example response:**
```json
{
  "modelo": "vader",
  "score": 0.8555,
  "sentimiento": "Positivo",
  "texto": "This product is amazing!"
}
```

---

## 📊 Project Structure

```
.
├── src/                # Source code
│   └── app.py
├── tests/              # (Optional) Tests
├── docs/               # Additional documentation
├── requirements.txt    # Python dependencies
├── README.md
├── LICENSE             # MIT License
└── .gitignore
```

---

## 🔧 Requirements

```bash
pip install -r requirements.txt
```

This project uses:
- Flask
- vaderSentiment
- textblob

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 📍 Author

Developed by **Hugo Canaval** as a practical project for sentiment analysis and backend deployment using Flask. Feel free to fork, extend, or use it in your own projects!

---

# API de Análisis de Sentimientos

Esta es una API REST simple construida con Flask para analizar reseñas de clientes usando dos modelos: **VADER** y **TextBlob**. La API recibe un texto y el modelo a usar, y devuelve un puntaje de polaridad y una clasificación de sentimiento.

---

## 📌 Características

- Soporte para dos modelos de análisis de sentimiento: **VADER** y **TextBlob**
- Devuelve un puntaje compuesto de polaridad y clasificación (Positivo, Negativo, Neutral)
- Fácil de integrar con Firebase, aplicaciones frontend o procesamiento por lotes

---

## 🚀 Cómo usarlo

### 1. Clona e instala el proyecto
```bash
git clone https://github.com/Hacanaval/customer-review-sentiment.git
cd sentiment-analysis-api
pip install -r requirements.txt
```

### 2. Ejecuta la API localmente
```bash
cd src
python app.py
```

### 3. Envía una petición POST a `/sentiment`
Puedes usar Postman, curl o fetch:
```json
{
  "text": "Este producto es excelente!",
  "model": "vader"
}
```

**Modelos válidos:** `vader`, `textblob`

**Ejemplo de respuesta:**
```json
{
  "modelo": "vader",
  "score": 0.8555,
  "sentimiento": "Positivo",
  "texto": "Este producto es excelente!"
}
```

---

## 📊 Estructura del Proyecto

```
.
├── src/                # Código fuente
│   └── app.py
├── tests/              # (Opcional) Pruebas
├── docs/               # Documentación adicional
├── requirements.txt    # Dependencias de Python
├── README.md
├── LICENSE             # Licencia MIT
└── .gitignore
```

---

## 🔧 Requisitos

```bash
pip install -r requirements.txt
```

Este proyecto usa:
- Flask
- vaderSentiment
- textblob

---

## 📄 Licencia

Este proyecto está licenciado bajo la **Licencia MIT**. Ver [LICENSE](LICENSE) para más detalles.

---

## 📍 Autor

Desarrollado por **Hugo Canaval** como un proyecto práctico para el análisis de sentimientos y despliegue backend usando Flask. ¡Siéntete libre de hacer fork, extenderlo o usarlo en tus propios proyectos!

