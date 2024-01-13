""" This file contains the code for the chatbot response. """

# Importing the required libraries and model
import nltk
import pickle
import numpy as np
import json
import random
from nltk.stem import WordNetLemmatizer
from keras.models import load_model
from googletrans import Translator  # Import Translator from googletrans module
from flask import Flask
from flask_socketio import SocketIO, emit

lemma = WordNetLemmatizer()
model = load_model('model.h5')
intents = json.loads(open('intents.json').read())
words = pickle.load(open('word.pkl','rb'))
classes = pickle.load(open('class.pkl','rb'))

# Function to clean up the sentence
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemma.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# Function to create the bag of words
def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    cltn = np.zeros(len(words), dtype=np.float32)
    for word in sentence_words:
        for i, w in enumerate(words):
            if w == word:
                cltn[i] = 1
                if show_details:
                    print(f"Found '{w}' in bag")
    return cltn

# Function to predict the class
def predict_class(sentence, model):
    l = bow(sentence, words, show_details=False)
    res = model.predict(np.array([l]))[0]

    ERROR_THRESHOLD = 0.25
    results = [(i, j) for i, j in enumerate(res) if j > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = [{"intent": classes[k[0]], "probability": str(k[1])} for k in results]
    return return_list

# Function to get the response
def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    for i in intents_json['intents']:
        if i['tag'] == tag:
            return random.choice(i['responses']) 

# Function to translate messages
def translate_message(message, source_language, target_language='en'):
    translator = Translator()
    translated_message = translator.translate(message, src=source_language, dest=target_language).text
    return translated_message

# Function to get the chatbot response 
def chatbotResponse(msg, source_language):
    translated_msg = translate_message(msg, source_language)
    ints = predict_class(translated_msg, model)
    res = getResponse(ints, intents)
    translated_response = translate_message(res, 'en', source_language)
    
    return translated_response

# Creating the flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.static_folder = 'static'
socketio = SocketIO(app, cors_allowed_origins="*")

# Creating the socket connection
@socketio.on('message')
def handle_message(data):
    source_language = data['language']
    response = chatbotResponse(data['message'], source_language)
    print(response)
    emit('recv_message', response)

# Running the app
if __name__ == "__main__":
    socketio.run(app, debug=True)
