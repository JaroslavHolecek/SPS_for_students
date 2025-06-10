import numpy as np
import tensorflow as tf

# Načtení dat
X = np.load("train_data.npy")
y = np.load("train_labels.npy")

# Definice modelu
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(7,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(4, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Trénování modelu
model.fit(X, y, epochs=20, batch_size=32)

# Uložení modelu
model.save("auticko_model.h5")
