# -*- coding: utf-8 -*-
"""
Created on Thu May 20 14:09:10 2021

@author: kAwTaR
"""

from nltk.corpus import stopwords
from nltk import word_tokenize,FreqDist
from nltk.tokenize import sent_tokenize
import re,xlrd,string
import matplotlib.pyplot as plt

#ouvrir les fichiers
#les fichiers de la langue francaise 

fichier = open("Ce que je crois.txt","r", encoding='utf-8')
fichier=fichier.read()

#print(fichier)
#segmentation en mot 
#eliminer les ponctuation
 
s =fichier.translate(str.maketrans(string.punctuation, " "*len(string.punctuation))) 

#eliminer les stops words

stop_words = stopwords.words("french")
#segmenter en mot
word_tokens = word_tokenize(s.strip())
filtered_word = [w for w in word_tokens if not w in stop_words]
print("segmenter en mot:",filtered_word)
#segmentation en phrase

sent_tokens=sent_tokenize(fichier, language="french")
print("segmenter en phrase",sent_tokens)

#ouvrir les fichiers
#les fichiers de la langue arab

fichier_a = open("الصاروخ الصيني.txt","r", encoding='utf-8')
fichier_a=fichier_a.read()

#eliminer les ponctuation

a =fichier_a.translate(str.maketrans(string.punctuation, " "*len(string.punctuation)))
#print(a)
#eliminer les stops words

stop_words= stopwords.words('arabic')

#segmenter en mot 

word_tokens = word_tokenize(a.strip())
filtered_word_a = [w for w in word_tokens if not w in stop_words]
print("segmenter en mot:",filtered_word_a)

#segmenter en phrase
sent_tokens_a = sent_tokenize(fichier_a)
print("segmenter en phrase:  ",sent_tokens_a)


#lire fichier excel

inf_excel = xlrd.open_workbook("inf.xlsx",encoding_override="utf-8")

#extraire les information du fichier excel 

feuille_1 = inf_excel.sheet_by_index(0)
cols = feuille_1.ncols
rows = feuille_1.nrows

X = []
Y= []
Z= []
V=[]
W=[]
#pour text en francais 
for r in range(0, rows):
    X += [feuille_1.cell_value(rowx=r, colx=0)]
    Y += [feuille_1.cell_value(rowx=r, colx=1)]
    Z += [feuille_1.cell_value(rowx=r, colx=2)]
#print(X,Y,Z)    
print(sent_tokens[0])
if sent_tokens[0]== "text1.":
    print(X[0],":",Y[0],"\n",X[1],":",Y[1],"\n",X[2],":",Y[2])
else :
    print(X[0],":",Z[0],"\n",X[1],":",Z[1],"\n",X[2],":",Z[2])

#pour text en arab 

for r in range(0, rows):
    V += [feuille_1.cell_value(rowx=r, colx=3)]
    W += [feuille_1.cell_value(rowx=r, colx=4)]
#print(X,V,W)    
print(sent_tokens_a[0])
if sent_tokens_a[0]== "النص1.":
    print(X[0],":",V[0],"\n",X[1],":",V[1],"\n",X[2],":",V[2])
else :
    print(X[0],":",W[0],"\n",X[1],":",W[1],"\n",X[2],":",W[2])

#calculer freq des mots txt en francais 

freq = FreqDist(filtered_word)
freq.plot(30)
print("graphe des freq des mots txt en francais: ",freq)

#calculer la longeur des fichier francais (mot)

longeur_m=len(filtered_word)
print("la longeur des fichier francais (mot):",longeur_m)

#calculer la longeur des fichier francais (caractère)

longeur_c=len(fichier)
print("la longeur des fichier francais (caractère):",longeur_c)
      
#calculer freq des mots txt en arab

freq_a = FreqDist(filtered_word_a)
freq_a.plot(30)
print("graphe des freq des mots txt en arabe :",freq_a)

#calculer la longeur des fichier arab (mot)

longeur_m_a=len(filtered_word_a)
print("la longeur des fichier francais (mot):",longeur_m_a)

#calculer la longeur des fichier francais (caractère)

longeur_c_a=len(fichier_a)
print("la longeur des fichier francais (caractère):",longeur_c_a)

#calculer la longeur maximale des mots francais
    
b=[]
for i in range(longeur_m) :
    a=filtered_word[i]
    #print(a)
    b +=[ len(a)]
#print(b)

C=max(b)
print("la longeur maximale des mots francais:",C)
 
#calculer la longeur maximale des mots arabes
    
b=[]
for i in range(longeur_m_a) :
    a=filtered_word_a[i]
    #print(a)
    b +=[ len(a)]
#print(b)

C=max(b)
print("la longeur maximale des mots arabes:",C)
       









































































