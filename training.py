import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tensorflow.keras import layers
from tensorflow.keras import Model
import pandas as pd
import numpy as np
from tensorflow.keras.optimizers import RMSprop

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

train_dir = 'train'
valid_dir = 'validation'

#######################################################
######       Validation des repartitions         ######
#######################################################

# nombre de chiens par race dans le set d'entrainement
train_df = pd.DataFrame([{
    "name": d,
    "count": len(os.listdir(os.path.join(train_dir, d)))
} for d in os.listdir(train_dir)])

# nombre de chiens par race dans le set d'evaluation
valid_df = pd.DataFrame.from_dict([{
    "name": d,
    "count": len(os.listdir(os.path.join(valid_dir, d)))
} for d in os.listdir(valid_dir)])

fig, ax = plt.subplots(figsize=(50,50))
x = np.arange(len(train_df['name'].values))

width = 0.35
rects1 = ax.bar(x - width/2, train_df['count'].values, width, label='Train')
rects2 = ax.bar(x + width/2, valid_df['count'].values, width, label='Validation')

ax.set_ylabel('Number of dogs')
ax.set_title('Number of dogs per breed')
ax.set_xticks(x)
ax.set_xticklabels(train_df['name'].values, rotation='vertical')
ax.legend()

fig.tight_layout()
plt.show()

#######################################################
######           Creation du model               ######
#######################################################

# 150x150 for the image pixels, and 3 for color channels: R, G, and B
img_input = layers.Input(shape=(150, 150, 3))

# Convolution and MaxPooling2D (16 filters)
x = layers.Conv2D(16, 3, activation='relu')(img_input)
x = layers.MaxPooling2D(2)(x)

# Convolution and MaxPooling2D (32 filters)
x = layers.Conv2D(32, 3, activation='relu')(x)
x = layers.MaxPooling2D(2)(x)

# Convolution and MaxPooling2D (64 filters)
x = layers.Conv2D(64, 3, activation='relu')(x)
x = layers.MaxPooling2D(2)(x)

# Flatten feature map to a 1-dim tensor so we can add fully connected layers
x = layers.Flatten()(x)

# Create a fully connected layer with ReLU activation and 512 hidden units
x = layers.Dense(512, activation='relu')(x)

# Dropout layer
x = layers.Dropout(0.5)(x)

# Create output layer with a single node and softmax activation
output = layers.Dense(120, activation='softmax')(x)

# Create model
model = Model(img_input, output)

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(lr=0.001),
              metrics=['acc'])


#######################################################
######           Data Preprocessing              ######
#######################################################

from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        train_dir,  
        target_size=(150, 150),
        batch_size=20,
        classes=valid_df.name.values.tolist())

validation_generator = val_datagen.flow_from_directory(
        valid_dir,
        target_size=(150, 150),
        batch_size=20,
        classes=valid_df.name.values.tolist())

history = model.fit_generator(
      train_generator,
      steps_per_epoch=int(14458 / 20),
      epochs=30,
      validation_data=validation_generator,
      validation_steps=int(6122 / 20),
      verbose=2)


#######################################################
######           Sauvegarde du model             ######
#######################################################
model.save("model_1.h5")

#######################################################
######           Calcule de Precision            ######
#######################################################
acc = history.history['acc']
val_acc = history.history['val_acc']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'b')
plt.plot(epochs, val_acc, 'r')
plt.title('Training and validation accuracy')

plt.show()


