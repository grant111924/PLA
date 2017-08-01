# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 13:44:24 2017

@author: DELL

Pocket PLA 跑2000 
trainig dataset:

testing dataset:

"""

import numpy as np

def openFile(fileName,dataList):
    f=open(fileName,'r')
    x=0
    for line in f:
        y=line.split()
        y=list(map(float,y))
        dataX=[]
        y.insert(0,1)
        dataX.append(y[0:5])
        dataX.append(y[5])
        dataList.append(dataX)
        x+=1
    f.close    
def sign(t):
    if t>0:
        return 1
    else:
        return -1
def mui(error,data):
    tmpData=[]
    for i in range(5):
        tmpData.append(error*data[i])
        i+=1
    return tmpData   
def add(x,y):
    temp=[]
    for i in range(5):
        temp.append(x[i]+y[i])
        i+=1
    return temp   
def dot(w,data):
      temp=0
      speed=0.5
      #w0=-1 #   +(-threshold)*x0  if x0=1, threshold=1
      for i in range(5):
        temp=temp+w[i]*data[i]*speed
        i+=1
      #temp+=w0
      return temp   

def getErrorRate(w,dataList):
    n = len(dataList);  
    error=0
    for i in range(0,n):
        data =dataList[i]
        fact=data[1]
        compute=sign(dot(w,data[0]))
        if fact != compute:
            error+=1
    return error/n

def pocket_pla(dataList,normalW,pocketW,Finish):
     itertion=1#修正錯誤次數
     index=0 # 計算到第幾個樣本
     while itertion<Finish:
         data=dataList[index] 
         fact=data[1]
         compute=sign(dot(normalW,data[0]))
         #print('fact %d compute %d'%(fact,compute))
         if fact != compute:
             normalW=add(normalW,mui(fact,data[0]))
             nErrorRate=getErrorRate(normalW,dataList)
             pErrorRate=getErrorRate(pocketW,dataList)
             if nErrorRate<pErrorRate:
                pocketW=normalW
             itertion+=1

             
         if index==len(dataList)-1:
              index=0
         else:
              index+=1
     return pocketW
             

                

dataListTrain=[]
dataListTest=[]
fileNameTrain="hw1_18_train.txt"
fileNameTest="hw1_18_test.txt"
openFile(fileNameTrain,dataListTrain)
openFile(fileNameTest,dataListTest)
normalW=[0,0,0,0,0]
pocketW=[0,0,0,0,0]

 
testErrorTotal=0
for i in range(2000):
    np.random.shuffle(dataListTrain)# 隨機點開始 
    pocketW=pocket_pla(dataListTrain,normalW,pocketW,50)
    trainingError = getErrorRate(pocketW,dataListTrain);  
    testError = getErrorRate(pocketW,dataListTest);  
    testErrorTotal+=testError    
    print(pocketW)         
    print('第 %d 次 Training錯誤率 %f Testing錯誤率 %f' %(i,trainingError,testError))
average=testErrorTotal/2000
print('平均修正次數: %f' %(average)) 
