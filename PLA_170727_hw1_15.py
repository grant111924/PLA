# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:46:16 2017

@author: DELL

完成 2017/7/30 

"""
import numpy as np


def sign(t):
    if t<=0:
        return -1
    else:
        return 1

     
def naive_pla(dataX,dataY):
    #初始化 設定  
     Finish=False
     w=[0,0,0,0,0] 
     itertion=0#修正錯誤次數
     index=0 # 計算到第幾個樣本 
     correctNum=0 #當前正確樣本數

     while Finish != True:
         fact =dataY[index]
         compute=sign(np.dot(w,dataX[index]))
         if fact==compute:
             correctNum+=1
         else:
             #w(t+1)=w(t)+y(t)*x(t)
            w+=np.multiply(fact,dataX[index])
            itertion+=1
            correctNum=0
            print('找到第%d 個錯誤，經過：%d 次運算' %(index,itertion))
         
         if index==len(dataX)-1:
              index=0
         else:
              index+=1
              
         if correctNum==len(dataX):
             Finish=True
     print('成功找到最佳解  總共 %d 次運算'%(itertion))

dataX=[] # X特徵值
dataY=[] # Y結果-1 or +1
x=0
f=open("hw1_15_train.txt",'r')
for line in f:
    y=line.split()
    y=list(map(float,y))
    y.insert(0,1)# 放入W0的權重值[w0,w1,w2,w3,w4]
    dataX.append(y[0:5])
    dataY.append(y[5])
    x+=1
f.close 
naive_pla(dataX,dataY)


