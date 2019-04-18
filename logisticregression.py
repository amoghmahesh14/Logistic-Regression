#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 12:59:14 2019

@author: amogh
"""

from sklearn import tree
import csv
import numpy as np
'''features = [[140,1],[130,1],[150,0],[170,0]]
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
print(clf.predict([[150,1]]))'''

fp = open('ex2data1.txt' , 'r')
reader = csv.reader(fp , delimiter=',')
dataset = []
for row in reader:
	dataset.append(row)

data = np.array(dataset)
X=data[:,0:2]
y=data[:,2]
clf = tree.DecisionTreeClassifier()
clf=clf.fit(X,y)
result=clf.predict([[90,90]])
if result is 0:
    print ("Fail")
else:
    print("Pass")