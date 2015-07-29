# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:48:42 2015

@author: Anton Kulesh
"""
# Строится векторная модель документов коллекции. Используется мера TF-IDF.
# Каждый вектор отражает важность слов(=термов) в документе.
# При сравнение документов используется косинусная мера.
# Предварительно необходимо установить библиотеки: nltk, gensim.

import nltk.corpus
import nltk.stem
import nltk, re, pprint, csv
from nltk import word_tokenize
from gensim import corpora, models, similarities
stemmer_func = nltk.stem.snowball.SnowballStemmer("english").stem
stopwords = set(nltk.corpus.stopwords.words('english'))

def csv_open(filename):
    f=open(filename, 'rb')
    reader = csv.reader(f)
    s=[]
    for row in reader:
        s.append(row)
    return s

def doc_list(collection_name):
    entities=csv_open(collection_name)
    docs=[]
    for Type,Name,Desc in entities:
        docs.append(Desc)        #Список документов (утверждений)
    return docs
    
def normalize_word(word):
    return stemmer_func(word.lower()) #Стемминг слов
    
def get_tokens(documents):
    token_lists=[[normalize_word(word) for word in word_tokenize(document) if word not in stopwords] for document in documents]
    return token_lists  #Получение списка токенов для каждого документа
    
def main_terms(documents):  # Выделение ключевых слов из каждого документа
    token_lists=get_tokens(documents)
    texts = [[w for w in token_list if len(w)>2 and not w in stopwords and w.isalpha()] for token_list in token_lists]
    all_tokens=[item for sublist in texts for item in sublist]
    texts = [[w for w in text if all_tokens.count(w)>1] for text in texts]
    return texts

def dict(documents,path,name):  # Создание словаря терминов
    terms=main_terms(documents)
    dictionary = corpora.Dictionary(terms)
    dictionary.save(path+'\\'+name+'.dict') #Сохранение словаря на диск
    return dictionary
    

def corp(documents,path,name): # Создание корпуса
    dictionary=dict(documents,path,name)
    terms=main_terms(documents)
    corpus = [dictionary.doc2bow(term) for term in terms]
    corpora.MmCorpus.serialize(path+'\\'+name+'.mm', corpus) #Сохранение корпуса
    return corpus    

#Сравнение документов (пример)    
docs=doc_list('Collection.csv')
path= 'E:\\Ontology\\workspace'
name='ontology'
corpus=corp(docs,path,name)
num_features=len(dict(docs,path,name))

#Сравним 3-й документ коллекции со всеми остальными и выведем номера документов,
#которые с данным документом имеют меру "схожести" > 0.2.
tfidf = models.TfidfModel(corpus)
vec = corpus[2]
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features)
sims = index[tfidf[vec]]

for (doc,sim) in list(enumerate(sims)):
    if 0.99>sim>0.2:
        print (doc+1,sim) #Вывод: (номер документа, мера "схожести" с ним)
    
  

   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    