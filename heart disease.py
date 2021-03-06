# -*- coding: utf-8 -*-
"""Patient Heart Disease.ipynb
"""

#1. Import the packages
from sklearn import preprocessing
import tensorflow as tf
from tensorflow import keras
from keras import layers, optimizers, losses, metrics
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from keras.callbacks import EarlyStopping, TensorBoard
import datetime, os
import pandas as pd

# Commented out IPython magic to ensure Python compatibility.
# Load the TensorBoard notebook extension
# %load_ext tensorboard

# Load the csv file using pd.read_csv
df = pd.read_csv(r"/content/heart.csv")

# print head of the dataframe
df.head

#3. Data preprocessing
# Split data into features and labels
features = df.copy()
labels = features.pop('target')

#One-hot encode for all the categorical features
features = pd.get_dummies(features)

#Convert dataframe into numpy array
features = np.array(features)
labels = np.array(labels)

#Perform train-test split
SEED=0
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=SEED)

#Data normalization
scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

#4. Build a NN that overfits easily
nIn = x_test.shape[-1]
nClass = len(np.unique(y_test))

model = keras.Sequential()
model.add(layers.InputLayer(input_shape=(nIn,)))
model.add(layers.Dense(4096, activation='relu'))
model.add(layers.Dense(4096, activation='relu'))
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(nClass, activation='softmax'))

#5. View your model
model.summary()

tf.keras.utils.plot_model(model, show_shapes=True)

#6. Compile model
BATCH_SIZE = 128
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

tf.keras.backend.clear_session()

from gc import callbacks
import datetime, os
logdir = os.path.join("logs", datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
tensorboard_callback = tf.keras.callbacks.TensorBoard(logdir, histogram_freq=1)

#train the model
BATCH_SIZE= 100
EPOCHS = 100
history = model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=BATCH_SIZE, epochs= EPOCHS, callbacks=[tensorboard_callback])

# Commented out IPython magic to ensure Python compatibility.
# View training accuracy and loss graph via tensorboard
# %tensorboard --logdir logs

# evaluate the model
model.evaluate(x_test, y_test, verbose=2)

tf.keras.backend.clear_session()

# predict the model
np.argmax(model.predict(np.expand_dims(x_test[100], axis=0)))

#plot the graph error 
import matplotlib.pyplot as plt

# plot the graph of training loss vs val_loss
training_loss = history.history['loss']
val_loss = history.history['val_loss']
epoch = history.epoch

plt.plot(epoch, training_loss, label = 'Training Loss')
plt.plot(epoch, val_loss, label = 'Validation Loss')
plt.title('Training vs Validation Loss')
plt.legend()
plt.xlabel('epochs')
plt.ylabel('error')
plt.show()

#plot the graph of training accuracy vs validation loss
training_accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']
epoch = history.epoch

plt.plot(epoch, training_accuracy, label = 'Training Accuracy')
plt.plot(epoch, val_accuracy, label = 'Validation Accuracy')
plt.title('Training vs Validation Accuracy')
plt.legend()
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.show()
