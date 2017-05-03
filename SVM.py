# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 14:57:42 2017

@author: Admin
"""

from sklearn import svm
from sklearn.metrics import accuracy_score
import PreProcessData
import GetTestSet

X, Y = PreProcessData.get_xy()
#print(X)
#print(Y)

X_test, Y_test = GetTestSet.get_xy_test()

rbf_kernel = svm.SVC(kernel='rbf', gamma=0.05, C=1.0).fit(X, Y)
poly_kernel = svm.SVC(kernel='poly', degree=3, C=1.0).fit(X, Y)
linear_kernel = svm.SVC(kernel='linear', C=1.0).fit(X, Y)

pred_linear = linear_kernel.predict(X_test).tolist()
pred_rbf = rbf_kernel.predict(X_test).tolist()
pred_poly = poly_kernel.predict(X_test).tolist()

print(accuracy_score(Y_test, pred_rbf))
print(accuracy_score(Y_test, pred_poly))
print(accuracy_score(Y_test, pred_linear))

while(True):
    path = input('Please Enter Path File: ')
    path_news = ''
    for s in path:
        if(s == '/'):
            s = s + '\\'
        else:
            s = s + s
    raw = open(path, encoding='utf-8').read()
    news_features = PreProcessData.get_features(raw)
    linear_pred = linear_kernel.predict(news_features).tolist()
    rbf_pred = rbf_kernel.predict(news_features).tolist()
    poly_pred = poly_kernel.predict(news_features).tolist()
    print('Linear Model ' + linear_pred[0])
    print('RBF Model ' + rbf_pred[0])
    print('Polynomial Pred ' + poly_pred[0])
    