from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import numpy as np
import os
from PIL import Image
import keras

GET = 'GET'
POST = 'POST'

app = Flask(__name__, template_folder='.')

@app.route('/', methods=[GET])
def home():
    return render_template("index.html")

@app.route('/recognize_picture', methods=[POST])
def recognize_image():
    data = request.files['dog_picture']
    img = Image.open(data) # chargement avec Pillow
    filename = 'image.'+img.format
    img.save(filename)
    keras.preprocessing.image.load_img(filename, target_size=(224,224))
    predict = 
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)