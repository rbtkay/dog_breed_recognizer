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

GET = 'GET'
POST = 'POST'

app = Flask(__name__, template_folder='.')

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

img_dir = "validation"

@app.route('/', methods=[GET])
def home():
    return render_template("index.html")

@app.route('/', methods=[POST])
def recognize_image():
    data = request.files['dog_picture']
    if not data:
        return render_template("index.html", error="Une image est requise.")
    img = Image.open(data) # chargement avec Pillow
    filename = 'image.'+img.format
    img.save(filename)
    current_image = keras.preprocessing.image.load_img(filename, target_size=(150, 150))

    dog_breeds = [d for d in os.listdir(img_dir)]

    model = load_model("model_1.h5")
    predictions = model.predict((np.expand_dims(current_image, 0)))
    os.remove(filename)

    return render_template("index.html", breed=dog_breeds[np.argmax(predictions[0])])

if __name__ == "__main__":
    app.run(debug=True)
