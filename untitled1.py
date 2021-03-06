# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OJz3Rqj4g0T6R7Ct4Y-z7k8JLA66oS29
"""

import pandas as pd
import numpy as np
import re
import math
import time
from google.colab import drive

# Commented out IPython magic to ensure Python compatibility.
#Tensorflow Libraries
try:
#   % tensorflow_version 2.x
except:
  pass
import tensorflow as tf
from tensorflow.keras import layers
import tensorflow_datasets as tfds

#Fetyching data from drive
drive.mount("/content/drive")

cols=["sentiment","id","date","query","user","text"]
train=pd.read_csv("/content/drive/My Drive/Data/train.csv",
           
          header=None, names=cols,engine="python",encoding="latin1")

test=pd.read_csv("/content/drive/My Drive/Data/test.csv",
           
          header=None, names=cols,engine="python",encoding="latin1")

train.head(3)

def clean_tweet(tweet):
  tweet=BeautifulSoup(tweet,"lxml").get_text()
  tweet=re.sub(r"@a-zA-Z0-9]+"," ",tweet)
  tweet=re.sub(r"https?://[a-zA-Z0-9./]+"," ",tweet)
  tweet=re.sub(r"[a-zA-Z.!?']"," ",tweet)
  tweet=re.sub(r" +"," ",tweet)
  return tweet

test_clean=[clean_tweet(tweet) for tweet in train.text]
train_clean=[clean_tweet(tweet) for tweet in test.text]
data_clean=[clean_tweet(tweet) for tweet in data.text]

data_labels=train.sentiment.values
data_labels[data_labels==4]=1
set(data_labels)

tokenizer=tfds.features.text.SubwordTextEncoder.build_from_corpus(data_clean,target_vocab_size=2**16)
data_input=tokenizer.encode(x) for x in data_clean

maxlength1=max(len(sent) for sent in input])
data_input=tf.keras.preprocessing.siquence.pad_sequences(data_input,value=0,padding='post',maxlen=maxlenght1)

test_data=np.randint(0,8000000,80000) #The first half have negative tweets and secod half have postive tweets
test_data=test_data.concatenate(test_data+8000000) #Second half is added to the first half randomly accessed numbers
test_input=data_input(test_data) #choose input data
test_label=data_labels(test_data) #give labes to the test set

#Remove this from train set to get the reamining data as train set
train_input=np.delete(data_input,test_data,axis=0)
train_labels=np.delete(data_labels,test_data)

class DCNN(tf.keras.models):
  def __init__(self,
               vocab_size,
               emb_dim=128,
               nb_filters=50,
               FNN_units=512,
               nb_classes=2,
               dropout_rate=0.2,
               training=False,
               name='DCNN'):
    super(DCNN,self).__init__(name=name)
    self.embedding=layers.embedding(vocab_size,emb_dim)
    self.bigram.Layers.Conv1D(filters=nb_filters,
                              kernel_size=2,
                              padding="valid",
                              activation="relu")
    self.pool1=layers.GlobalMaxPool1D()
    self.tigram.Layers.Conv1D(filters=nb_filters,
                              kernel_size=3,
                              padding="valid",
                              activation="relu")
    self.pool2=layers.GlobalMaxPool1D()
    self.fourgram.Layers.Conv1D(filters=nb_filters,
                              kernel_size=4,
                              padding="valid",
                              activation="relu")
    self.pool3=layers.GlobalMaxPool1D()


    self.dense_1=layers.Dense(units=FFN_units,activation="relu")
    self.dropout=layers.Dropout(rate=dropout_rate)

    if nb_classes==2:
      self.last_dense=layers.Dense(units=1,activation="sigmoid")
    else:
      self.dense_last=layers.Dense(units=nb.nb_classes,activation="softmax")

def call(self,input,train):
  self.embedding(input)
  x1=self.bigram(x)
  x1=self.pool1(x1)
  x2=self.trigram(x)
  x2=self.pool1(x2)
  x3=self.fourgram(x)
  x3=self.pool1(x3)
  merged=tf.conact(x_1,x_2,x_3,axis=1)
  merged=self.dense_1(merged)
  merged=self.dropout(merged,train)
  output=self.last_dense(merged)

  return output

#CONFIGURATION

Vocab_size=tokenizer.vocab_size
Emb_dim=200
NB_filters=100
FFN_units=256
NB_classes=len(set(train))
Dropout_rate=0.2
Batch_size=32
NP_epochs=5

#TRAINING

Dcnn=DCNN(vocab_size=Vocab_size,
emb_dim=Emb_dim
nb_filters=NB_filters
ffn_units=FFN_units
nb_classes=NB_classes
Dropout_rate=Dropout_rate
)

if NB_classes==2:
  Dcnn.compile(optimizer="adam",
               loss="binary_crossentropy",
               metrics="accuracy")

else:
  Dcnn.compile(optimizer="adam",
               loss="sparse_categorical_crossentropy",
               metrics="sparse_categorical_accuracy")
  

Dcnn.fit(train,batch_size=Batch_size),np_epochs=Np_epochs)

results=Dcnn.evaluate(test,test_labes,batch_size=Batch_size)