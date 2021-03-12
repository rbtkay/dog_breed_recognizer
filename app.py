from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import numpy as np
import os
import uuid
from PIL import Image
from tensorflow import keras 
from tensorflow.keras.models import load_model
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
from breeds import breeds

GET = 'GET'
POST = 'POST'

MODEL_FILE = 'vgg16_model.h5'

app = Flask(__name__, template_folder='.')

@app.route('/', methods=[GET])
def home():
    return render_template("index.html")

@app.route('/', methods=[POST])
def recognize_image():
    data = request.files['dog_picture']
    if not data:
        return jsonify({'error': "Une image est requise."})
    
    if not os.path.exists(MODEL_FILE):
        return jsonify({
            'error': f"Un export de model nommé {MODEL_FILE} doit être intégré à vos fichiers."
        })
    
    config = ConfigProto()
    config.gpu_options.allow_growth = True
    session = InteractiveSession(config=config)
    
    img = Image.open(data) # chargement avec Pillow
    filename = f'{str(uuid.uuid1())}.{img.format}'
    img.save(filename)
    current_image = keras.preprocessing.image.load_img(filename, target_size=(224, 224))

    model = load_model(MODEL_FILE)
    predictions = model.predict((np.expand_dims(current_image, 0)))
    os.remove(filename)

    breed = breeds[np.argmax(predictions[0])].split('-')
    breed.pop(0)
    breed = ' '.join(breed).replace('_',' ')
    return jsonify({'breed': breed})

if __name__ == "__main__":
    app.run(debug=True)
