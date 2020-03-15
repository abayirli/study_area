import tensorflow as tf 
from tensorflow import keras

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.5
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

import numpy as np 

# Set CPU as available physical device
my_devices = tf.config.experimental.list_physical_devices(device_type='CPU')
tf.config.experimental.set_visible_devices(devices= my_devices, device_type='CPU')
print(my_devices)
X = np.array([1,2,3,4,5])
y = np.array([3,5,7,9,11])

l0 = keras.layers.Dense(units = 1, input_shape = [1])
model = tf.keras.Sequential([l0])
model.compile(loss = "mean_squared_error", optimizer = tf.keras.optimizers.Adam(0.1))

history = model.fit(X, y, epochs = 500, verbose = False)

print(model.predict([6]))