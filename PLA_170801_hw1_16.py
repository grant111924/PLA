# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 09:00:34 2017

@author: DELL

PLA 跑2000
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

   
def naive_pla(dataList):
     Finish=False
     w=[0,0,0,0,0]
     itertion=0#修正錯誤次數
     index=0 # 計算到第幾個樣本
     correctNum=0 #當前正確樣本數
     while Finish!=True:
         data=dataList[index] 
         fact=data[1]
         compute=sign(np.dot(w,data[0]))
         if fact == compute:
            correctNum+=1
         else:
             w=w+np.multiply(fact,data[0])      #w(t+1)=w(t)+y(t)*x(t)
             correctNum=0
             itertion+=1
             
         if index==len(dataList)-1:
              index=0
         else:
              index+=1
              
         if correctNum == len(dataList):
            Finish=True
            print('完成一次修正')
       
     return  itertion 
             

                 
def main():
    dataList=[]
    fileName="hw1_15_train.txt"
    openFile(fileName,dataList)
    totalStep=0
    for i in range(2000):
        np.random.shuffle(dataList)# 隨機點開始 
        step=naive_pla(dataList)
        totalStep+=step  
        print('第 %d 次 修正次數: %d' %(i,step))
    average=totalStep/2000
    print('平均修正次數: %d' %(average)) 


main()    