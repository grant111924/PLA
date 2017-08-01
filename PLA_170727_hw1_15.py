# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:46:16 2017

@author: DELL

完成 2017/7/30 

"""
#import numpy as np


dataX=[]
dataY=[]
x=0
w0=-1
f=open("hw1_15_train.txt",'r')
for line in f:
    y=line.split()
    y=list(map(float,y))
    y.insert(0,1)
    dataX.append(y[0:5])
   # print(dataX)
    dataY.append(y[5])
    #print(dataY)
    x+=1
f.close 


def sign(t):
    if t<=0:
        return -1
    else:
        return 1
def add(x,y):
    for i in range(5):
        x[i]=x[i]+y[i]
        i+=1

def mui(error,data):
    tmpData=[]
    for i in range(5):
        tmpData.append(error*data[i])
        i+=1
    return tmpData   
def dot(w,data):
      temp=0
      for i in range(5):
        temp=temp+w[i]*data[i]
        i+=1
      return temp
     
def naive_pla(dataX,dataY):
    #初始化 設定  
     Finish=False
     w=[0,0,0,0,0]
     itertion=0#修正錯誤次數
     index=0 # 計算到第幾個樣本 
     correctNum=0 #當前正確樣本數

     while Finish != True:
         fact =dataY[index]
         compute=sign(dot(w,dataX[index]))
         if fact==compute:
             correctNum+=1
         else:
             #w(t+1)=w(t)+y(t)*x(t)
            add(w,mui(fact,dataX[index]))
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
naive_pla(dataX,dataY)


