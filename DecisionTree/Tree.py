# -*- coding:utf-8 -*-
from math import log
import numpy as np
import matplotlib.pyplot as plt
import operator
from TreePlotter import createPlot
def createDataSet():       #表3-1数据建模
    dataSet = [['水','脚蹼','鱼'],
               ['水','无蹼','鱼'],
               ['水','脚蹼','非鱼'],
               ['陆','脚蹼','非鱼'],
               ['陆','脚蹼','非鱼'],
               ]
    labels = ['水里生存','脚蹼']
    return dataSet,labels
def calcuEntropy(dataSet):   #度量数据集的无序程度，熵值越高，则混合的数据越多
    numbers = len(dataSet)
    labelCount = {}     #{'鱼': 2, '非鱼': 3}
    for line in dataSet:
        currentLabel = line[-1]
        if currentLabel not in labelCount.keys():
            labelCount[currentLabel] = 0
        labelCount[currentLabel] += 1
    entropy = 0.0
    for key in labelCount:
        lableProbability = float(labelCount[key])/numbers  #类别出现概率
        entropy -= lableProbability *log(lableProbability,2)
    return entropy
def splitDataSet(dataSet,column,value): #以数据集dataSet每行第column列的特征value划分
    splitData = []
    for line in  dataSet:
        if line[column] ==  value:
            before= line[:column]
            after=line[column+1:]
            before.extend(after)  #a=[1,2] b=[3,4] a.extend(b) [1,2,3,4] a.append [1,2,[3,4]]
            splitData.append(before)
    return splitData
def chooseBestFeatureToSplit(dataSet):
    numLabels = len(dataSet[0]) - 1  #取出第一行数据：['水','脚蹼','鱼']  计算其个数 3
    baseEntropy = calcuEntropy(dataSet)
    bestInfoGain = 0.0  #最好的信息增益
    bestFeature = -1   #返回最好的特征的 索引值（列）
    for i in range(numLabels):
        featList = [line[i] for line in dataSet]  # 分别取出第一列：水 水 水 陆 陆，第二列：脚蹼  无蹼  脚蹼  脚蹼  脚蹼
        uniFeatList = set(featList)                # c创建唯一分类标签类别，去除重复标签得：水 陆 无蹼  脚蹼
        newEntropy = 0.0
        for value in uniFeatList:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob*calcuEntropy(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]#stop splitting when all of the classes are equal
    if len(dataSet[0]) == 1: #stop splitting when there are no more features in dataSet
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]       #copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree
if __name__ == '__main__':
    dataSet,labels=createDataSet()
    tree=createTree(dataSet,labels)
    print tree
    # entropy= calcuEntropy(dataSet)
    # # print  labelCount['鱼']
    # kk=splitDataSet(dataSet,0,'水')
    # for line in kk:
    #    print '特征: %s,标签: %s' % (line[0], line[1])
    # kk=chooseBestFeatureToSplit(dataSet)
    # print kk
    # for line in kk:
    #    print  line
