# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:48:42 2015

@author: Anton Kulesh
"""
# Строится векторная модель документов коллекции. Используется мера TF-IDF.
# Каждый вектор отражает важност слов(=термов) в документе.
# Предварительно необходимо установить библиотеки: nltk, gensim.

import nltk.corpus
import nltk.stem
import nltk, re, pprint, csv
from nltk import word_tokenize
from gensim import corpora, models, similarities
stemmer_func = nltk.stem.snowball.SnowballStemmer("english").stem
stopwords = set(nltk.corpus.stopwords.words('english'))

################################ Подготовка данных ############################
mystopwords=['whose','also','one','two','three','four','speak','call']
for w in mystopwords:
    stopwords.add(w)

# Загрузка csv-коллекции    
def csv_open(filename):
    f=open(filename, 'rb')
    reader = csv.reader(f)
    s=[]
    for row in reader:
        s.append(row)
    return s

# Создание списков с названиями документов и их описаниями
def docs_list(collection_name):
    entities=csv_open(collection_name)
    names,docs=[],[]
    for Type,Name,Keys,Desc in entities:
        names.append(Name)        # Список названий документов 
    for Type,Name,Keys,Desc in entities:
        docs.append(Desc)        # Список документов (утверждений)
    return [names,docs]
    
# Нормализация токенов (слов)
def normalize_word(word):
    return stemmer_func(word.lower())

# Получение списка токенов документа    
def get_tokens(doc):
    token_list=[normalize_word(word) for word in word_tokenize(doc) if word not in stopwords]
    return token_list  
    
# Выделение основных слов (термов) из каждого документа
def main_terms(docs): 
    token_lists=[get_tokens(doc) for doc in docs]
    texts = [[w for w in token_list if w not in stopwords if len(w)>2 and w.isalpha() or w in re.findall(r'[a-z]+\-[a-z]+',w)] for token_list in token_lists]
    if len(docs)!=1:
        all_tokens=[item for sublist in texts for item in sublist]
        terms = [[w for w in text if all_tokens.count(w)>1] for text in texts]
    else: terms=texts
    return terms

# Создание словаря терминов
def dic(docs,path='E:\\Ontology\\workspace',name='ontology'):  
    terms=main_terms(docs)
    dictionary = corpora.Dictionary(terms)
    dictionary.save(path+'\\'+name+'.dict') #Сохранение словаря на диск
    print '''The dictionary is created!\nTo open enter:\ndictionary = corpora.Dictionary.load(path+'\\\\'+name+'.dict')\n'''

# Необходимо указать путь к Вашей рабочей папке и придумать название для словаря(корпуса)
path= 'E:\\Ontology\\workspace'
name='ontology'     

# Создание корпуса
def corp(docs,path='E:\\Ontology\\workspace',name='ontology'): 
    dictionary = corpora.Dictionary.load(path+'\\'+name+'.dict')
    terms=main_terms(docs)
    corpus = [dictionary.doc2bow(term) for term in terms]
    corpora.MmCorpus.serialize(path+'\\'+name+'.mm', corpus) #Сохранение корпуса
    print '''The corpus is created!\nTo open enter:\ncorpus = corpora.MmCorpus(path+'\\\\'+name+'.mm')\n'''   

############################ Сравнение документов #############################  

docs=docs_list('Collection.csv')[1]
dic(docs)
corp(docs)
 
# Для заданного документа(doc) из документов всей коллекции (docs) выбираются документы, которые на него(doc) "похожи".  
# Для сравнения документов можно использовать модели 'tfidf'('1') или 'lsa'('2','lsi'). Также можно указать желаемую точность алгоритмя 0<accuracy<1
def sim_docs(doc,docs,accuracy=0.2,model="tfidf",path='E:\\Ontology\\workspace',name='ontology'):
    corpus = corpora.MmCorpus(path+'\\'+name+'.mm')
    dictionary = corpora.Dictionary.load(path+'\\'+name+'.dict')
# Преобразование документа в вектор
    doc_terms=main_terms([doc])[0]
    vec=dictionary.doc2bow(doc_terms)
# Создание tfidf-модели корпуса    
    tfidf = models.TfidfModel(corpus,id2word=dictionary) 
# Использование первой модели
    if model.lower()=="tfidf" or model=='1':
        index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary))
        sims = sorted(enumerate(index[vec]), key=lambda item: -item[1])
        sims = [(doc,sim) for (doc,sim) in sims if sim>accuracy]
# Использование второй модели; создание "обёрки" вокруг tfidf      
    elif model.lower()=="lsa" or model.lower()=="lsi" or model=='2':
        lsi = models.LsiModel(tfidf[corpus], id2word=dictionary, num_topics=20)
        corpus_lsi = lsi[tfidf[corpus]]
        vec_lsi=lsi[vec]
        index = similarities.SparseMatrixSimilarity(corpus_lsi,num_features=len(dictionary))
        sims = sorted(enumerate(index[vec_lsi]), key=lambda item: -item[1])
        sims = [(doc,sim) for (doc,sim) in sims if sim>accuracy]
# Если список "похожих" документов пуст, то алгоритм возвращает -1       
    if sims!=[]:
        return sims[1:]
    else: return -1

####################### Выделение ключевых слов ###############################
    
def key_words(doc,docs,num=4,path='E:\\Ontology\\workspace',name='ontology'):
    corpus = corpora.MmCorpus(path+'\\'+name+'.mm')
    dictionary = corpora.Dictionary.load(path+'\\'+name+'.dict')
# Создание tfidf-модели корпуса. Преобразование документа в tfidf-вектор
    tfidf = models.TfidfModel(corpus,id2word=dictionary)
    doc_terms=main_terms([doc])[0]
    vec=dictionary.doc2bow(doc_terms)
# Координаты вектора(vec) имеют вид (term,weight), где term - номер термина в словаре, weight - вес данного слова в документе
# Сортировка координат вектора(vec) по весу ("важности")
    tfidf_vec=sorted(tfidf[vec], key=lambda item: -item[1])
# Формирование упорядоченного списка ключевых слов
    key_terms=[dictionary[key] for (key,_) in tfidf_vec] 
# Если искомый список оказался пуст, то возвращается значение -1
    if key_terms!=[]:
        if len(key_terms)<=3 or len(key_terms)<=num:
            return key_terms
        else: return key_terms[:num]
    else: return -1

        
        



    
    
    
    
    
    
    