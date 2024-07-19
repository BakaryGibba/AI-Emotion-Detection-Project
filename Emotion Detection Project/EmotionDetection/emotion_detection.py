import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    try:
        response = requests.post(url, json=myobj, headers=headers)
        response.raise_for_status()
        emotion_scores = response.json().get('document', {}).get('emotion', {})

        # Extract scores and determine dominant emotion
        scores = {emotion: emotion_scores.get(emotion, 0.0) for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']}
        dominant_emotion = max(scores, key=scores.get)

        # Add dominant emotion to the scores dictionary
        scores['dominant_emotion'] = dominant_emotion
        return scores
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
