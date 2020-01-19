#!/usr/bin/env python
# coding: utf-8

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

#Loading the emotions dataset
dataset = pd.read_csv("../Datasets/Positive_thoughts/emotion.data")
dataset = dataset[dataset.emotions == "joy"]
# dataset = pd.concat([dataset[dataset.emotions == "joy"][:7000], dataset[dataset.emotions == "sadness"][:7000]])
dataset = dataset.drop(dataset.columns[0], 1)

# Loading reddit dataset
r_dataset = pd.read_csv("../Datasets/Negative_thoughts/reddit_posts.txt", sep="\n", header=None)
r_dataset.columns = ["text"]
r_dataset["emotions"] = ["sadness" for i in range(len(r_dataset))]
dataset = pd.concat([dataset[:len(r_dataset)], r_dataset])

# print(len(dataset[dataset.emotions=="joy"]), len(dataset[dataset.emotions=="sadness"])) 

input_sentences = [text.split(" ") for text in dataset["text"].values.tolist()]
labels = dataset["emotions"].values.tolist()

# Make ID Labels

word2id = dict()
id2word = dict()
label2id = dict()

max_words = 0 # maximum number of words in a sentence

# Construction of word2id dict
for sentence in input_sentences:
    for word in sentence:
        # Add words to word2id dict if not exist
        if word not in word2id:
            _id = len(word2id)
            word2id[word] = _id
            id2word[_id] = word
    # If length of the sentence is greater than max_words, update max_words
    if len(sentence) > max_words:
        max_words = len(sentence)

# Construction of label2id and id2label dicts
label2id = {l: i for i, l in enumerate(set(labels))}
id2label = {v: k for k, v in label2id.items()}

import keras
from keras.optimizers import Adam

# Encode input words and labels
X = [[word2id[word] for word in sentence] for sentence in input_sentences]
Y = [label2id[label] for label in labels]

# Apply Padding to X
from keras.preprocessing.sequence import pad_sequences
X = pad_sequences(X, max_words)

# Convert Y to numpy array
Y = keras.utils.to_categorical(Y, num_classes=len(label2id), dtype='float32')

# # Print shapes
print("Shape of X: {}".format(X.shape))
print("Shape of Y: {}".format(Y.shape))

import pickle
to_save = [word2id, max_words, id2label]
f = open("joy_reddit_vars", "wb")
pickle.dump(to_save, f)
f.close()

# Setup LSTM

# embedding_dim = 100 # The dimension of word embeddings

# # Define input tensor
# sequence_input = keras.Input(shape=(max_words,), dtype='int32')

# # Word embedding layer
# embedded_inputs = keras.layers.Embedding(len(word2id) + 1,
#                                         embedding_dim,
#                                         input_length=max_words)(sequence_input)

# # Apply dropout to prevent overfitting
# embedded_inputs = keras.layers.Dropout(0.2)(embedded_inputs)

# # Apply Bidirectional LSTM over embedded inputs
# lstm_outs = keras.layers.wrappers.Bidirectional(
#     keras.layers.LSTM(embedding_dim, return_sequences=True)
# )(embedded_inputs)

# # Apply dropout to LSTM outputs to prevent overfitting
# lstm_outs = keras.layers.Dropout(0.2)(lstm_outs)

# # Attention Mechanism - Generate attention vectors
# input_dim = int(lstm_outs.shape[2])
# permuted_inputs = keras.layers.Permute((2, 1))(lstm_outs)
# attention_vector = keras.layers.TimeDistributed(keras.layers.Dense(1))(lstm_outs)
# attention_vector = keras.layers.Reshape((max_words,))(attention_vector)
# attention_vector = keras.layers.Activation('softmax', name='attention_vec')(attention_vector)
# attention_output = keras.layers.Dot(axes=1)([lstm_outs, attention_vector])

# # Last layer: fully connected with softmax activation
# fc = keras.layers.Dense(embedding_dim, activation='relu')(attention_output)
# output = keras.layers.Dense(len(label2id), activation='softmax')(fc)

# # Finally building model
# model = keras.Model(inputs=[sequence_input], outputs=output)
# model.compile(loss="binary_crossentropy", metrics=["accuracy"], optimizer=Adam(lr=0.001))

# # # Print model summary
# # print("> Summary")
# # model.summary()

# model.fit(X, Y, epochs=2, batch_size=64, validation_split=0.1, shuffle=True)
# print("Finished Training")
# model.save("./joy_sad_msg_flag_epochs=2, batch_size=64, validation_split=0.1.hd5")
# print("Saved!")
