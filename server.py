"""
Flask web server for emotion detection application.
Serves a web interface for analyzing user input text
and detecting emotions using a pre-built model.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the homepage with the input form."""
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detection():
    """Process input text and return detected emotions."""
    text_to_analyze = request.values.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5001)
