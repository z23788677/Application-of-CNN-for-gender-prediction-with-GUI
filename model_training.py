import cv2
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dropout, Input, Conv2D, Dense, Flatten
from tensorflow.keras.models import Model

train_path = "Training"
vaildation_path = "Validation"

#normalized
train = ImageDataGenerator(rescale = 1/255)
vaildation = ImageDataGenerator(rescale = 1/255)

train_dataset = train.flow_from_directory(train_path,
                                          batch_size=5,
                                          target_size=(64, 64),
                                          class_mode = "binary")


vaildation_dataset = vaildation.flow_from_directory(vaildation_path,
                                          batch_size=5,
                                          target_size=(64, 64),
                                          class_mode = "binary")

i = Input(shape = (64, 64, 3))
x = Conv2D(16, (3, 3),  strides= 2, activation = "relu") (i)
x = Conv2D(32, (3, 3),  strides= 2, activation = "relu") (x)
x = Conv2D(64, (3, 3),  strides= 2, activation = "relu") (x)
#x = Conv2D(128, (3, 3),  strides= 2, activation = "relu") (x) (For 128 input)
x = Flatten () (x)
x = Dense(512, activation = "relu") (x)
x = Dense(2, activation = "softmax") (x)

model = Model(i, x)

model.compile(loss = "sparse_categorical_crossentropy",
              optimizer = "adam",
              metrics = ["accuracy"])

stop_early = tf.keras.callbacks.EarlyStopping(monitor='accuracy', patience=6)

r = model.fit(train_dataset , validation_data = vaildation_dataset, steps_per_epoch = 1000, epochs = 80, callbacks = [stop_early])

plt.plot(r.history["accuracy"], label = "acc")
plt.plot(r.history["val_accuracy"], label = "val_acc")
plt.legend()
plt.show()

plt.plot(r.history["loss"], label = "loss")
plt.plot(r.history["val_loss"], label = "val_loss")
plt.legend()
plt.show()

model.save("gender.h5")
print("The model has been saved!")