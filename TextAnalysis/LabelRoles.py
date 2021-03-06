#Performing Semantic Role Labelling 
#Author: Sanjana Pukalay

#NLTK and Practnlptools used for Analysis and SRL

import os
import nltk
from nltk.corpus import wordnet as wn
from practnlptools.tools import Annotator
import csv
import traceback
from nltk import stem
import re 

#Pre-defining a set of desired verbs

path = "C:/Users/hp/Desktop/bigdata/txt/"
data = []
verb_file = open("./set3.txt", "rw+") 
desired_verbs = verb_file.readlines()

#Performing Stemming

stemmed_desired_verbs=[]
stemmer=stem.snowball.EnglishStemmer()

for word in desired_verbs:
    stemmed_desired_verbs.append(stemmer.stem(word))
   
annotator=Annotator()

#Implementation of Semantic Role Labelling

f = open('out.csv', 'wt')
csv.register_dialect('lineterminator',lineterminator='\n')
writer = csv.writer(f, dialect = csv.get_dialect('lineterminator'))
writer.writerow( ('A0', 'A1', 'V', 'fileName'))
for filename in os.listdir(path):
    print 'reading', filename
    text_file = open(path + filename,"r")
    file_content = text_file.readlines()
    data.append((filename,file_content))
    text_file.close()

#Annotating the striped text
    
    for t1 in file_content:
        for text in t1.split("."):
            text.strip()
            if text:
                try:
                    x = annotator.getAnnotations(text)['srl']
                    for x_tuple in x:
                        a0 = None
                        a1 = None
                        v = None 
                        for item in x_tuple:
                            if item == 'A0':
                                a0 = x_tuple['A0']
                            if item == 'A1':
                                a1 = x_tuple['A1']
                            if item == 'V':
                                if stemmer.stem(x_tuple['V']) in stemmed_desired_verbs:
                                    v = x_tuple['V']
                        if (a0 is not None and a1 is not None and v is not None):
                            writer.writerow( (x_tuple['A0'], x_tuple['A1'], x_tuple['V'], filename))
                except Exception as e:
                    traceback.print_exc()
    f.flush()                
#Annotated text returned as output
