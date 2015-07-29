# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:27:41 2015

@author: Anton Kulesh
"""
#Начальный вариант коннектера. 

import re 
import csv
from neo4jAPI import addEntity, addRelation, updateEntity, getId, getType, getName 

#Данная функция загружает csv документ и возвращает его содержимое в виде списка
def csv_open(filename):
    f=open(filename, 'rb')
    reader = csv.reader(f)
    s=[]
    for row in reader:
        s.append(row)
    return s
    
listOfdata=csv_open('Collection.csv') #Загрузка коллекции из файла
for Type,Name,Description in listOfdata:
    addEntity(Type, Name, Description) #Добавление всех узлов в базу

for Type,Name,Description in listOfdata:
    for T,N,D in listOfdata:
        if Name.lower() in D.lower() and Name!=N:
            addRelation(getId(Name), getId(N)) #Между двумя узлами создается отношение Using_in, 
#если название (Name) одного из них содержится в описании (Description) другого узла.

#!!! Не работает, если в "утверждении" содержатся специальные символы (например \xc6\x92)            