from __future__ import print_function

# tag::mcts_go_cnn_processing[]
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D


def softmax(x):
    e_x = np.exp(x)
    e_x_sum = np.sum(e_x)
    return e_x / e_x_sum


x = np.array([100, 100])
print(softmax(x))

np.random.seed(123)
X = np.load('dlgo/generated_games/features-20.npy')
Y = np.load('dlgo/generated_games/labels-20.npy')

samples = X.shape[0]
size = 9
input_shape = (size, size, 1)  # <2>

X = X.reshape(samples, size, size, 1)  # <3>

train_samples = int(0.9 * samples)
X_train, X_test = X[:train_samples], X[train_samples:]
Y_train, Y_test = Y[:train_samples], Y[train_samples:]

# <1> We import two new layers, a 2D convolutional layer and one that flattens its input to vectors.
# <2> The input data shape is 3-dimensional, we use one plane of a 9x9 board representation.
# <3> We then reshape our input data accordingly.
# end::mcts_go_cnn_simple_preprocessing[]

# tag::mcts_go_cnn_simple_model[]
model = Sequential()
model.add(Conv2D(filters=48, kernel_size=(3, 3),
                 activation='relu',
                 padding='same',
                 input_shape=input_shape))
model.add(Dropout(rate=0.5))
model.add(Conv2D(48, (3, 3),
                 padding='same', activation='relu'))  # <3>
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(rate=0.5))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(rate=0.5))
model.add(Dense(size * size, activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
# <1> The first layer in our network is a Conv2D layer with 32 output filters.
# <2> For this layer we choose a 3 by 3 convolutional kernel.
# <3> The second layer in another convolution. We leave out the "filters" and "kernel_size" arguments for brevity.
# <4> We then flatten the 3D output of the previous convolutional layer...
# <5> ... and follow up with two more dense layers, as we did in the MLP example.
# end::mcts_go_cnn_simple_model[]

# tag::mcts_go_cnn_simple_eval[]
model.fit(X_train, Y_train,
          batch_size=64,
          epochs=100,
          verbose=1,
          validation_data=(X_test, Y_test))
score = model.evaluate(X_test, Y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
# end::mcts_go_cnn_eval[]
