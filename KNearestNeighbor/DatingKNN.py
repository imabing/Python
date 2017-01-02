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
        # ȥ��β������\n
        line=line.strip()
        # �Կո�\t���ָ�������
        listFromline = line.split('\t')
        maxtrix[index,:] = listFromline[0:3]
        labels.append(int(listFromline[-1]))
        index += 1
    # ��ͼ
    # fig=plt.figure()
    # ax=fig.add_subplot(111)
    # ax.scatter(maxtrix[:,1],maxtrix[:,2])
    # plt.show()
    return maxtrix,labels
# ��һ����(��ǰֵ-��Сֵ)/(���ֵ-��Сֵ)
def normalize(dataSet):
    maxVal=dataSet.max(0)
    minVal=dataSet.min(0)
    ranges=maxVal-minVal
    dataSize = dataSet.shape[0]
    subMatrix = np.zeros(np.shape(dataSet))
    subMatrix=dataSet - np.tile(minVal,(dataSize,1))
    subMatrix = subMatrix / np.tile(ranges, (dataSize, 1))
    return  subMatrix,ranges,minVal
# ������ȷ��
def testErrorRatio():
    ratio=0.1
    errorRatio=0.0
    # ��ȡ����Դ��
    maxtrix, labels = fileToMatrix('datingTestSet2.txt')
    # ��һ��
    subMatrix, ranges, minVal=normalize(maxtrix)
    # ��¼������
    total=subMatrix.shape[0]
    # ���Լ�����
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