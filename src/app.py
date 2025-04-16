from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

app = Flask(__name__)
vader_analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def home():
    return "API de Análisis de Sentimiento funcionando 👋"

@app.route('/sentiment', methods=['POST'])
def sentiment():
    data = request.get_json()
    text = data.get('text')
    model = data.get('model', 'vader').lower()

    if not text:
        return jsonify({'error': 'Texto no recibido'}), 400

    if model == 'vader':
        score = vader_analyzer.polarity_scores(text)['compound']
    elif model == 'textblob':
        score = TextBlob(text).sentiment.polarity
    else:
        return jsonify({'error': 'Modelo no válido'}), 400

    if score > 0.05:
        label = 'Positivo'
    elif score < -0.05:
        label = 'Negativo'
    else:
        label = 'Neutral'

    return jsonify({
        'texto': text,
        'modelo': model,
        'score': score,
        'sentimiento': label
    })

if __name__ == '__main__':
    app.run(debug=True)
