# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 20:38:50 2015

@author: Anton Kulesh
"""

import csv
import re
#Данная функция принимает на входе список (listOfdata=результат работы парсера) "утверждений", обрабатывает каждое 
#из них по определенному шаблону и записывает результат в файл "Collection.csv" (создание коллекции)

def collection(listOfdata,filename="Collection.csv"):
    csvfile=open(filename, 'w')
    fieldnames = ['Type', 'Name','Description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(0,len(listOfdata)):
        if listOfdata[i][0]=='T':
            patt_theorem=r'Theorem\s[0-9]+\.[0-9]?\.?\s\([a-zA-Z\s\,\-]*\)\.?|Theorem\s[0-9]+\.[0-9]?\.?'
            name_theorem=re.findall(patt_theorem,listOfdata[i])
            disc_theorem=[listOfdata[i].replace(name_theorem[0],"")]
            if '(' in name_theorem[0]:
                name_theorem=re.findall(r'\((.*?)\)',name_theorem[0])  
                p_theorem=r'\)\.?\s?(.*?)\.$'
                disc_theorem=re.findall(p_theorem,listOfdata[i])
            writer.writerow({'Type': 'Theorem', 'Name': name_theorem[0],'Description':disc_theorem[0]})
        elif listOfdata[i][0]=='D':
            patt_def=r'Definition\s[0-9]+\.[0-9]?\.?\s\([a-zA-Z\s\,\-]*\)|Definition\s[0-9]+\.[0-9]?\.?'
            name_def=re.findall(patt_def,listOfdata[i])
            disc_def=[listOfdata[i].replace(name_def[0],"")]
            if '(' in name_def[0]:
                name_def=re.findall(r'\((.*?)\)',name_def[0])  
                p_def='\)\.?\s?(.*?)\.$'
                disc_def=re.findall(p_def,listOfdata[i])
            writer.writerow({'Type': 'Definition', 'Name': name_def[0],'Description':disc_def[0]})
        elif listOfdata[i][0]=='L':
            patt_lemma=r'Lemma\s[0-9]+\.[0-9]?\.?\s\([a-zA-Z\s\,\-]*\)|Lemma\s[0-9]+\.[0-9]?\.?'
            name_lemma=re.findall(patt_lemma,listOfdata[i])
            disc_lemma=[listOfdata[i].replace(name_lemma[0],"")]
            if '(' in name_lemma[0]:
                name_lemma=re.findall(r'\((.*?)\)',name_lemma[0])  
                p_lemma='\)\.?\s?(.*?)\.$'
                disc_lemma=re.findall(p_lemma,listOfdata[i])
            writer.writerow({'Type': 'Lemma', 'Name': name_lemma[0],'Description':disc_lemma[0]})
        
     