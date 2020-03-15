import tensorflow as tf 
from tensorflow import keras
import numpy as np 
import tensorflow_datasets as tfds 
import math


import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.5
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

#load dataset

dataset, metadata = tfds.load("fashion_mnist", as_supervised = True, with_info = True)
train_dataset, test_dataset = dataset["train"], dataset["test"]

print("dataset loaded!")

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal',      'Shirt',   'Sneaker',  'Bag',   'Ankle boot']

num_train_examples = metadata.splits["train"].num_examples 
num_test_examples = metadata.splits["test"].num_examples

print(f"Train samples: {num_train_examples} - Test samples: {num_test_examples}")


def normalize(images, labels):
	images = tf.cast(images, tf.float32)
	images /= 255

	return images, labels

train_dataset = train_dataset.map(normalize)
test_dataset = test_dataset.map(normalize)

train_dataset = train_dataset.cache()
test_dataset = test_dataset.cache()


model = keras.Sequential([keras.layers.Conv2D(32, (3,3), padding = "same", activation = tf.nn.relu),
						  keras.layers.MaxPooling2D((2,2), strides = 2),
						  keras.layers.Conv2D(64, (3,3), padding = "same", activation =  tf.nn.relu),
						  keras.layers.MaxPooling2D((2,2), strides = 2),
						  keras.layers.Flatten(),
						  keras.layers.Dense(units = 128, activation = tf.nn.relu),
						  keras.layers.Dense(units = 10, activation = tf.nn.softmax)
						  ])

model.compile(optimizer = "adam", loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=["accuracy"])

BATCH_SIZE = 32
train_dataset = train_dataset.cache().repeat().shuffle(num_train_examples).batch(BATCH_SIZE)
test_dataset = test_dataset.cache().batch(BATCH_SIZE)


model.fit(train_dataset, epochs=10, steps_per_epoch=math.ceil(num_train_examples/BATCH_SIZE))

test_loss, test_accuracy = model.evaluate(test_dataset, steps=math.ceil(num_test_examples/BATCH_SIZE))

print(f"CNN - Accuracy on the test set: {test_accuracy}")