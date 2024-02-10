""" This file is used to train the model and save it as model.h5 file. """

# Importing the required libraries
import nltk
import json
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
import random
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
lemma = WordNetLemmatizer()

# Preprocessing the data
words=[]
classes = []
docs = []
ignore_words = ['?', '!','',"'"]
data_file = open('intents.json').read()
intents = json.loads(data_file)

# Tokenizing the words
for i in intents['intents']:
    for pattern in i['patterns']:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        docs.append((w, i['tag']))

        if i['tag'] not in classes:
            classes.append(i['tag'])

# Lemmatizing the words
words = [lemma.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# Sorting the classes
classes = sorted(list(set(classes)))

# Printing the length of the documents, classes and words
print (len(docs), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique lemmatized words", words)

# Saving the words and classes in pickle files
pickle.dump(words,open('word.pkl','wb'))
pickle.dump(classes,open('class.pkl','wb'))

# Creating the training data
training = []
output_empty = [0] * len(classes)

# Creating the bag of words
for d in docs:
    bag = []
    pattern_words = d[0]
    pattern_words = [lemma.lemmatize(word.lower()) for word in pattern_words]
    
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(d[1])] = 1
    
    training.append([bag, output_row])

# Shuffling the training data
random.shuffle(training)
training = np.array(training,dtype=object)

x_train = list(training[:,0])
y_train = list(training[:,1])
print("created Training data Succesfully")

# Creating the model : Sequential model
model = Sequential()
model.add(Dense(150, input_shape=(len(x_train[0]),), activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(150, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(len(y_train[0]), activation='softmax'))

# Compiling the model
sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Fitting the model
file = model.fit(np.array(x_train), np.array(y_train), epochs=250, batch_size=5, verbose=1)
model.save('model.h5', file)

print("Successful model creation")

# Evaluating the model
loss, accuracy = model.evaluate(np.array(x_train), np.array(y_train))
print('Accuracy:', accuracy)
print('Loss:',loss)