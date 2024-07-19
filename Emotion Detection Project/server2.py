from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy implementation for illustration
# Replace this with your actual emotion analysis logic
def emotion_analyzer(text):
    # Example response structure
    return {"label": "joy", "score": 0.85}

@app.route("/EmotionDetector")
def emotion_analyzer_route():
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return jsonify({"error": "Invalid input! Try again."}), 400

    response = emotion_analyzer(text_to_analyze)

    label = response.get('label')
    score = response.get('score')

    if label is None or score is None:
        return jsonify({"error": "Invalid response from emotion analyzer."}), 500

    return jsonify({"message": f"The given text has been identified as {label} with a score of {score}."})

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
