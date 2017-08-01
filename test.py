#encoding=utf8
import sys
import numpy as np
import math
from random import *

if __name__ == '__main__':
    # params
    TIMES = 2000
    sum_halts = 0
    SPEED = 0.5
    # read raw data
    raw_data = []
    for line in open("hw1_15_train.txt").readlines():
        raw_data.append(line.strip())
    # iteratively
    a = Random()
    for i in range(0,TIMES):
        W = [ 0.0, 0.0, 0.0, 0.0, 0.0 ]
        halts = 0
        # randomly shuffle data
        a.seed(i)
        a.shuffle(raw_data)
        # pla process
        for line in raw_data:
            items = line.strip().split('\t')
            print(items)
            y = items[1].strip()
            X = items[0].strip().split(' ')
            X.insert(0,1)
            print(X)
            # gurantee the length of W and X
            if ( len(W)!=len(X) ):
                sys.exit(-1)
            # initial score 0
            score = 0.0
            # calculate W'X
            for i in range(0,len(X)):
                score = score + float(X[i]) * float(W[i])
                print("i=%d X=%d W=%d"%(i,float(X[i]),float(W[i])))
            # transfer score to sign
            sign = 1 if score>0.0 else -1
            if sign != int(y) :
                halts = halts + 1
                for i in range(0,len(X)):
                    W[i] = float(W[i]) +float(y)*float(X[i])
        print ("halts:" + str(halts))
        # accumulate sum of halts
        sum_halts = sum_halts + halts
    print ("average halts:" + str(sum_halts/(TIMES-1)))