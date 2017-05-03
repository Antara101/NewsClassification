# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:48:42 2017

@author: Admin
"""
import nltk
import CreateListWord as clw

def count_word_in_it(l):
    path = 'C:/Users/Admin/Desktop/work/project-nlp/IT.txt'
    raw = open(path, encoding='utf-8').read()
    word_list = raw.split('\n')
    count_list = [w for w in l if w in word_list]
    return len(count_list)
       
def count_word_in_bs(l):
    path = 'C:/Users/Admin/Desktop/work/project-nlp/BS.txt'
    raw = open(path, encoding='utf-8').read()
    word_list = raw.split('\n')
    count_list = [w for w in l if w in word_list]
    return len(count_list)
    
def count_word_in_sport(l):
    path = 'C:/Users/Admin/Desktop/work/project-nlp/Sport.txt'
    raw = open(path, encoding='utf-8').read()
    word_list = raw.split('\n')
    count_list = [w for w in l if w in word_list]
    return len(count_list)

def get_features(news):
    list_word = news.split(' ')
    stopwords = nltk.corpus.stopwords.words('english')
    token = [w.lower() for w in list_word if w.lower() not in stopwords and w.isalpha()]
    set_word = set(token)
    return [count_word_in_bs(set_word),
            count_word_in_it(set_word),
            count_word_in_sport(set_word),         
            ]

def get_xy():
    it_path = clw.get_path_list('C:/Users/Admin/Desktop/work/project-nlp/bbc/tech/')
    bs_path = clw.get_path_list('C:/Users/Admin/Desktop/work/project-nlp/bbc/business/')
    sport_path = clw.get_path_list('C:/Users/Admin/Desktop/work/project-nlp/bbc/sport/')
    X = []
    Y = []
    for path in it_path:
        raw = open(path, encoding='utf-8').read()
        X.append(get_features(raw))
        Y.append('TECH')

    for path in bs_path:
        raw = open(path, encoding='utf-8').read()
        X.append(get_features(raw))
        Y.append('BUSISNESS')
    
    for path in sport_path:
        raw = open(path, encoding='utf-8').read()
        X.append(get_features(raw))
        Y.append('SPORT')
    return (X, Y)

    
    