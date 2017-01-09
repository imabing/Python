# -*- coding:utf-8 -*-
import numpy as np
def loadDataSet():
    # 1、语料库
    dataSet = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
               ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
               ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
               ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
               ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
               ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    # 类别
    labels = [0, 1, 0, 1, 0, 1]
    return dataSet, labels
    # 2、语料去重
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)   #并集
    return list(vocabSet)
# 3、把输入文本转换为一个与语料去重库同大小的行向量，并统计对应的词语个数
def setOfWords2Vec(vocabSet, inputSet):
    returnVec = [0] * len(vocabSet)
    for word in inputSet:
        if word in vocabSet:
            returnVec[vocabSet.index(word)] = 1
        else:
            print "the word: %s is not in my Vocabulary!" % word
    return returnVec


def trainNB0(trainMatrix, trainCategory):  #输入：语料库向量矩阵与标签
    numLine = len(trainMatrix)        #矩阵行数 6
    numWords = len(trainMatrix[0])     #矩阵列数 32
    p1 = sum(trainCategory) / float(numLine)   #语料中垃圾邮件 1 占的比重
    matrix0 = np.ones(numWords);   #构造初始值为1的矩阵，numpy.zeros初始值为0
    matrix1 = np.ones(numWords)  # change to ones()
    totalWord0 = 2.0;
    totalWord1 = 2.0
    for i in range(numLine):
        if trainCategory[i] == 1:
            matrix1 += trainMatrix[i]       #统计每个关键字出现的次数
            totalWord1 += sum(trainMatrix[i])  #每条记录关键字数累加
        else:
            matrix0 += trainMatrix[i]
            totalWord0 += sum(trainMatrix[i])
    p1Vect = np.log( matrix1 / totalWord1)  # matrix1 / totalWord1  每个关键字在该类中出现的概率
    p0Vect = np.log(matrix0 / totalWord0)  # change to log()
    return p0Vect, p1Vect, p1


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + np.log(pClass1)  # element-wise mult
    p0 = sum(vec2Classify * p0Vec) + np.log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    dataSet, labels = loadDataSet()            #原始语料
    vocabList = createVocabList(dataSet)       #关键字去重
    trainMat = []                              #把语料的每一个样本都转换为向量矩阵[[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1], [0, 0,...
    for line in dataSet:
        trainMat.append(setOfWords2Vec(vocabList, line))
    p0V, p1V, p1 = trainNB0(np.array(trainMat), np.array(labels))

    testEntry = ['love', 'my', 'dalmation','哈哈哈']
    thisDoc = np.array(setOfWords2Vec(vocabList, testEntry))
    print testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, p1)
    testEntry = ['stupid', 'garbage']
    thisDoc = np.array(setOfWords2Vec(vocabList, testEntry))
    print testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V,p1)


if __name__ == '__main__':
    testingNB()
    dataset, labels=loadDataSet()
    vocabSet=createVocabList(dataset)
