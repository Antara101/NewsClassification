# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 16:47:41 2017

@author: Admin
"""
import nltk

from urllib import request
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
print (type(raw))
print (len(raw))
print (raw.find("PART I"))
print (raw.rfind("End of Project Gutenberg’s Crime and Punishment"))

tokens = nltk.word_tokenize(raw)
print (type(tokens))
print (len(tokens))
tokens[:10]

text = nltk.Text(tokens)
print (type(text))
text[1020:1030]
text.collocations()

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = request.urlopen(url).read().decode('utf8')
html[:100]


from bs4 import BeautifulSoup
raw = BeautifulSoup(html).get_text()
#tokens = nltk.word_tokenize(raw)
#print (tokens)
tokens = nltk.word_tokenize(raw)
start = tokens.index("Blondes")
stop = tokens.index("friend")
print (start,stop)
tokens = tokens[start:stop]
text = nltk.Text(tokens)
text.concordance('gene')
text.collocations()

import nltk.book
f = open('Thailand.txt')
raw = f.read()
#print (raw)
list = raw.split(' ')
stopwords = nltk.corpus.stopwords.words('english')
token = [w for w in list if w not in stopwords]
fdist1 = FreqDist(token)
vocab1 = fdist1.keys()
print (fdist1.most_common(10))


path = nltk.data.find('corpora/gutenberg/melville-moby_dick.txt')
raw = open(path, 'r').read()
print (raw)

