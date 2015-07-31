# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:27:41 2015

@author: Anton Kulesh
"""
########################## Коннектер ##########################################

import re 
import csv
from neo4jAPI import* 
from docs_similarity import*
 
listOfdata=csv_open('Collection.csv') #Загрузка коллекции из файла
Names,Descriptions=docs_list('Collection.csv')[0],docs_list('Collection.csv')[1] #Списки названий документов и их описаний

#Добавление всех узлов в базу
def add_all(listOfdata):
    for Type,Name,Keys,Description in listOfdata:
        addEntity(Type, Name, Keys, Description) 

#Заполнеие поля keywords
def fill_keys(listOfdata,num):
    for Type,Name,Keys,Description in listOfdata:
        entityId,Keys,entityKeys=getId(Name),key_words(Description,Descriptions,num)," "
        if Keys!=-1:
            Keys=[w.encode("utf-8") for w in Keys]
            for w in Keys:
                entityKeys+=w+", "
            updateEntity(entityId, getType(entityId), Name,entityKeys, getDescription(entityId))

#Создание связей между сущностями            
def generate_relations(listOfdata):
    for Type,Name,Keys,Description in listOfdata:
        for T,N,K,D in listOfdata:
            if Name.lower() in D.lower() and Name!=N:
#Между двумя узлами создается отношение Using_in, если название (Name) одного из них содержится в описании (Description) другого узла.
                addRelation(getId(Name), getId(N))
#Если сущность_1-Using_in->сущность_2 и сущность_2-Using_in->сущность_1, то вместо данных связей между сущностями устанавливается Brother-связь
                if testDirectRelation(N,Name)==True and testDirectRelation(Name,N)==True and testDirectRelation(N,Name,"Brother")==False and testDirectRelation(Name,N,"Brother")==False:
                    removeRelation(getId(N), getId(Name))
                    removeRelation(getId(Name), getId(N))
                    addRelation(getId(Name), getId(N),"Brother")
#Similar-связь. Устанавливается на основании схожести сущностей (заданый параметры: accuracy=0.4, model='lsa')                
    for Type,Name,Keys,Description in listOfdata:       
        similar_docs=sim_docs(Description,Descriptions,0.4,'lsa')
        if similar_docs!=-1:
            for (doc,_) in similar_docs:            
                if testAnyRelation(Name,Names[doc])==False:
                    addRelation(getId(Name), getId(Names[doc]),"Similar")
                    
        
#!!! Алгоритм Не работает, если в "утверждении" содержатся специальные символы (например \xc6\x92)            