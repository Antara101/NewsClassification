# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:39:51 2017

@author: Admin
"""

import nltk
import unicodedata
from urllib import request

def get_path_list(path):
    word_list = []
    for i in range(350) :
        num_file = i + 1
        file_name = ''
        if(num_file > 99):
            file_name = str(num_file)
        elif(num_file > 9):
            file_name = '0' + str(num_file)
        else:
            file_name = '00' + str(num_file)
        path_file = path + file_name + '.txt'
        word_list.append(path_file)
    return word_list
        
def get_word_list(l):
    word_list = []
    for path in l:
        word_list_temp = []
        raw = open(path, encoding='utf-8').read()
        list_word = raw.split(' ')
        stopwords = nltk.corpus.stopwords.words('english')
        token = [w.lower() for w in list_word if w.lower() not in stopwords and w.isalpha()]
        set_word = set(token)
        for word in set_word:
            word_list_temp.append(word)
        word_list = word_list + word_list_temp
    return set(word_list)

def save_file(set_word, file_name):
    path = 'C:/Users/Admin/Desktop/work/project-nlp/' + file_name + '.txt'
    file = open(path, 'w')
    for word in set_word:
        w = word + '\n'
        file.write(w)
    file.close
        
    
it_path = get_path_list('C:/Users/Admin/Desktop/work/project-nlp/bbc/tech/')
bs_path = get_path_list('C:/Users/Admin/Desktop/work/project-nlp/bbc/business/')
sport_path =get_path_list('C:/Users/Admin/Desktop/work/project-nlp/bbc/sport/')

it_word_list = get_word_list(it_path)
business_word_list = get_word_list(bs_path)
sport_word_list = get_word_list(sport_path)

save_file(it_word_list, 'IT')
save_file(business_word_list, 'BS')
save_file(sport_word_list, 'Sport')
