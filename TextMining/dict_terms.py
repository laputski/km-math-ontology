# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:48:02 2015

@author: Anton Kulesh
"""
import nltk.corpus
import nltk.stem
import nltk, re, pprint
from nltk import word_tokenize
stemmer_func = nltk.stem.snowball.SnowballStemmer("english").stem
stopwords = set(nltk.corpus.stopwords.words('english'))
#ignorcharts='''.,<>/?!"';:[]{}\|+=()*&^%$_1234567890'''

from connecter import csv_open
entities=csv_open("Collection.csv")
docs=[]
for Type,Name,Desc in entities:
    docs.append(Desc)        #Список документов (утверждений)

def normalize_word(word):
    return stemmer_func(word.lower()) #Стемминг слов
    
def get_tokens(documents):
    tokens = []
    for document in documents:
        for token in document.split():
            tokens.append(normalize_word(token))
    return list(tokens)  #Получение списка токенов
    
def dict(documents):  # Создание словаря терминов
    tokens=get_tokens(documents)
    d_set=[token for token in tokens if len(token)>2 and not token in stopwords and token.isalpha()]
    d_set=[w for w in d_set if d_set.count(w)>1]
    return d_set
    

     