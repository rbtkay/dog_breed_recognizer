from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import numpy as np
import os
from PIL import Image
from tensorflow import keras 
from tensorflow.keras.models import load_model
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
from breeds import breeds

GET = 'GET'
POST = 'POST'

app = Flask(__name__, template_folder='.')

@app.route('/', methods=[GET])
def home():
    return render_template("index.html")

@app.route('/', methods=[POST])
def recognize_image():
    data = request.files['dog_picture']
    if not data:
        return render_template("index.html", error="Une image est requise.")
    
    config = ConfigProto()
    config.gpu_options.allow_growth = True
    session = InteractiveSession(config=config)
    
    img = Image.open(data) # chargement avec Pillow
    filename = 'image.'+img.format
    img.save(filename)
    current_image = keras.preprocessing.image.load_img(filename, target_size=(150, 150))

    model = load_model("model_1.h5")
    predictions = model.predict((np.expand_dims(current_image, 0)))
    os.remove(filename)

    return render_template("index.html", breed=breeds[np.argmax(predictions[0])])

if __name__ == "__main__":
    app.run(debug=True)
