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
validation_dir = 'test'

# train_data = []
# validation_data = []
train_data = [os.path.join(train_dir, d) for d in os.listdir(train_dir)]
validation_data = [os.path.join(validation_dir, d)
                   for d in os.listdir(validation_dir)]

#######################################################
######       Validation des repartitions         ######
#######################################################
# nombre de chiens par race dans le set d'entrainement
train_df = pd.DataFrame([{
    "name": d,
    "count": len(os.listdir(os.path.join(train_dir, d)))
} for d in os.listdir(train_dir)])

# nombre de chiens par race dans le set d'evaluation
test_df = pd.DataFrame.from_dict([{
    "name": d,
    "count": len(os.listdir(os.path.join(train_dir, d)))
} for d in os.listdir(train_dir)])

print(train_df)
print(test_df)