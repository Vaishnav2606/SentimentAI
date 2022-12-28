import numpy as np
import string
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
import pandas as pd
import pickle
import re


vectorizer = None 

with open('model/vect.pkl','rb') as file:
    vectorizer = pickle.load(file)

model = joblib.load('model/model')

#Pre-Processing Functions
def remove_pun_links(tweets):
    texts = tweets
    import string
    texts = re.sub(r'http\S+','', texts)
    texts = re.sub(r'\S+.com','', texts)        
    texts = texts.translate(str.maketrans('', '', string.punctuation))
    return texts

def word_split(tweet):
    text = tweet
    text = text.split()
    return text

def dictionarize_freq(words):
    word_count = ''
    dic = {}
    keys, values = np.unique(words, return_counts=True)
    for k, v in (zip(keys,values)):
        dic[k] = v
    word_count = (dic)
    return word_count

#Calling the functions for preprocessing
def preProcess(s):
    pun_removed =  remove_pun_links(s)
    words = word_split(pun_removed)
    word_count = [dictionarize_freq(words)]
    df = pd.DataFrame(np.array(word_count), columns=['word_count'])
    k = vectorizer.transform(df['word_count'])
    return k

#Prediction Function
def predict(x):
    a = model.predict(x)
    if(a[0]==0):
        print('Negative')
        return 'Negative'
    elif(a[0]==4):
        print('Positive')
        return 'Positive'
    else:
        print("Neutral")
        return 'Neutral'
    
#Taking input and predicting
def predRun(text):
    x = preProcess(text)
    x = predict(x)
    return x





