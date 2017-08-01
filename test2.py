# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:45:23 2017

@author: DELL
"""
import numpy as np

def file2matrix(filename,columline):
# 读取数据，从文件中读出来变成矩阵
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = np.ones((numberOfLines,columline+1))
    classLableVector =np.zeros((numberOfLines,1))
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split()
        returnMat[index,1:columline+1] = listFromLine[0:columline]
        classLableVector[index,0] =  float(listFromLine[-1])
        index += 1

    return  returnMat, classLableVector


data_Mat, dataLabels = file2matrix('hw1_15_train.txt', 4)

print(data_Mat)
print(dataLabels)