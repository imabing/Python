# -*- coding: cp936 -*-
import numpy as np
import os
from KNN import knn
def imgToMatrix(filename):
    matrix = np.zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            matrix[0,32*i+j] = int(lineStr[j])
    # [[0.  0.  0...., 0.  0.  0.]]
    return matrix
def readData(uri):
    labels = []
    # 打印文件名['0_0.txt', '0_1.txt', '0_10.txt', '0_100.txt', '0_101.txt',....
    fileList = os.listdir(uri)           #load the training set
    m = len(fileList)
    matrix = np.zeros((m,1024))
    for i in range(m):
        fileFullName = fileList[i]                 #0_0.txt
        fileName = fileFullName.split('.')[0]     # 0_0
        number = int(fileName.split('_')[0])      # 0
        labels.append(number)
        matrix[i,:] = imgToMatrix('%s/%s' % (uri,fileFullName))
    return matrix,labels

def test():
    error=0
    trainingMatrix,trainingLables=readData('trainingDigits')
    testMatrix, testLables = readData('testDigits')
    testNum=len(testLables)
    for i in  range(testNum):
        predictedLabel=knn(testMatrix[i,:],trainingMatrix,trainingLables,5)
        correctLabel = testLables[i]
        print 'predictedLabel: %d,correctLabel: %d' % (predictedLabel, correctLabel)
        if (predictedLabel != correctLabel):
            error += 1
    errorRatio = error / float(testNum)
    return  errorRatio
if __name__ == '__main__':
    # print imgToMatrix('trainingDigits/0_0.txt')
    # print readData('trainingDigits')
    print test()