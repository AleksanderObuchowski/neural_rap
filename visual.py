from Tkinter import *
window = Tk()
labelText = StringVar()



def callback():
    start = numpy.random.randint(0, len(dataX)-1)
    pattern = dataX[start]
    print ("Seed:")
    print ("\"", ''.join([int_to_char[value] for value in pattern]), "\"")
    # generate characters

    rap_line = ""
    labelText.set("generowanie nowego tekstu")
    for i in range(1000):
        x = numpy.reshape(pattern, (1, len(pattern), 1))
        x = x / float(n_vocab)
        prediction = model.predict(x, verbose=0)
        index = numpy.argmax(prediction)
        result = int_to_char[index]
        seq_in = [int_to_char[value] for value in pattern]
        sys.stdout.write(result)
        rap_line+=result
        pattern.append(index)
        pattern = pattern[1:len(pattern)]
    print("\nDone.")
    print("RAP LINE: ",rap_line)
    print(type(rap_line))
    labelText.set(rap_line)


## NN

import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils


filename = "rap_lyrics.txt"
raw_text = open(filename).read()[:1500000]
raw_text = raw_text.lower()
# create mapping of unique chars to integers
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
# summarize the loaded data
n_chars = len(raw_text)
n_vocab = len(chars)
print ("Total Characters: ", n_chars)
print ("Total Vocab: ", n_vocab)
# prepare the dataset of input to output pairs encoded as integers
seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
    seq_in = raw_text[i:i + seq_length]
    seq_out = raw_text[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])
    n_patterns = len(dataX)
print("Total Patterns: ", n_patterns)
# reshape X to be [samples, time steps, features]
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
# normalize
X = X / float(n_vocab)
# one hot encode the output variable
y = np_utils.to_categorical(dataY)
import sys


# define the LSTM model\n",
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')


 # load the network weights\n",
filename = "weights-improvement-01-1.6926.hdf5"
model.load_weights(filename)
model.compile(loss='categorical_crossentropy', optimizer='adam')

int_to_char = dict((i, c) for i, c in enumerate(chars))






title = Label(window,text = "Neural Rap",width = '200')
title.config(font=("Courier", 44))
title.pack()


#e = Entry(window,width = '200')
#e.insert(0, "wpisz poczatek tekstu")
#e.pack()
b = Button(window, text="generuj rap", width=10, command=callback)
b.pack()
rap = Label(window,textvariable  = labelText,width = '200',wraplength='800')
rap.config(font=("Courier", 24))
rap.pack()
window.mainloop()
