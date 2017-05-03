# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 15:47:22 2017

@author: Admin
"""
import PreProcessData as ppd

def get_path_list(path):
    word_list = []
    for i in range(350, 400) :
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
    
def get_xy_test():
    it_path = get_path_list('C:/Users/Admin/Desktop/work/project-nlp/bbc/tech/')
    bs_path = get_path_list('C:/Users/Admin/Desktop/work/project-nlp/bbc/business/')
    sport_path = get_path_list('C:/Users/Admin/Desktop/work/project-nlp/bbc/sport/')
    X = []
    Y = []
    for path in it_path:
        raw = open(path, encoding='utf-8').read()
        X.append(ppd.get_features(raw))
        Y.append('TECH')

    for path in bs_path:
        raw = open(path, encoding='utf-8').read()
        X.append(ppd.get_features(raw))
        Y.append('BUSISNESS')
    
    for path in sport_path:
        raw = open(path, encoding='utf-8').read()
        X.append(ppd.get_features(raw))
        Y.append('SPORT')
    return (X, Y)

