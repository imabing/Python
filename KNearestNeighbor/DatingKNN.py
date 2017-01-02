# -*- coding: cp936 -*-
import numpy as np
import matplotlib.pyplot as plt
from KNN import knn
def fileToMatrix(fileName):
    fr=open(fileName)
    arrayOfLines=fr.readlines()
    numOfLines=len(arrayOfLines)
    maxtrix=np.zeros((numOfLines,3))
    labels=[]
    index=0
    for line in arrayOfLines:
        # 去除尾部换行\n
        line=line.strip()
        # 以空格\t来分割数据项
        listFromline = line.split('\t')
        maxtrix[index,:] = listFromline[0:3]
        labels.append(int(listFromline[-1]))
        index += 1
    # 画图
    # fig=plt.figure()
    # ax=fig.add_subplot(111)
    # ax.scatter(maxtrix[:,1],maxtrix[:,2])
    # plt.show()
    return maxtrix,labels
# 归一化：(当前值-最小值)/(最大值-最小值)
def normalize(dataSet):
    maxVal=dataSet.max(0)
    minVal=dataSet.min(0)
    ranges=maxVal-minVal
    dataSize = dataSet.shape[0]
    subMatrix = np.zeros(np.shape(dataSet))
    subMatrix=dataSet - np.tile(minVal,(dataSize,1))
    subMatrix = subMatrix / np.tile(ranges, (dataSize, 1))
    return  subMatrix,ranges,minVal
# 测试正确率
def testErrorRatio():
    ratio=0.1
    errorRatio=0.0
    # 读取数据源？
    maxtrix, labels = fileToMatrix('datingTestSet2.txt')
    # 归一化
    subMatrix, ranges, minVal=normalize(maxtrix)
    # 记录集条数
    total=subMatrix.shape[0]
    # 测试集数量
    testNum=int(total*ratio)
    for i in range(testNum):
        predictedLabel=knn(subMatrix[i,:],subMatrix[testNum:total,:],labels[testNum:total],5)
        correctLabel=labels[i]
        print 'predictedLabel: %d,correctLabel: %d'  % (predictedLabel, correctLabel)
        if(predictedLabel!=correctLabel):
            errorRatio+=1.0
    errorRatio=errorRatio/float(testNum)
    print 'errorRatio is:%f' %errorRatio

def predicte(point):
    result = ['dislike', 'like', 'love']
    maxtrix, labels=fileToMatrix('datingTestSet2.txt')
    subMatrix, ranges, minVal = normalize(maxtrix)
    predictedLabel=knn((point-minVal)/ranges,subMatrix,labels,3)
    return result[predictedLabel-1];
if __name__ == '__main__':
    # maxtrix,labels=fileToMatrix('datingTestSet2.txt')
    # print maxtrix
    # print normalize(maxtrix)
    # testErrorRatio()
    point=[5000000,0,0]
    print predicte(point)