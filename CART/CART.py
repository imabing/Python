# -*- coding:utf-8 -*-
import numpy as np
def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine) #map all elements to float()
        dataMat.append(fltLine)
    return dataMat
def binSplitDataSet(dataSet, feature, value):
    mat0 = dataSet[np.nonzero(dataSet[:,feature] > value)[0],:]
    #print dataSet[np.nonzero(dataSet[:,feature] > value)[0],:]
    #print np.nonzero(dataSet[:,feature] > value)
    #print dataSet[np.nonzero(dataSet[:,feature] > value)[0],:].shape
    mat1 = dataSet[np.nonzero(dataSet[:,feature] <= value)[0],:]
    #print dataSet[np.nonzero(dataSet[:,feature] <= value)[0],:].shape
    return mat0,mat1
def regLeaf(dataSet):#returns the value used for each leaf
    return np.mean(dataSet[:,-1])
def regErr(dataSet):
    return np.var(dataSet[:,-1]) * np.shape(dataSet)[0]
def chooseBestSplit(dataSet, leafType=regLeaf, errType=regErr, ops=(1,4)):
    tolS = ops[0]; tolN = ops[1]
    #if all the target variables are the same value: quit and return value
    if len(set(dataSet[:,-1].T.tolist()[0])) == 1: #exit cond 1
        return None, leafType(dataSet)
    m,n = np.shape(dataSet)
    #the choice of the best feature is driven by Reduction in RSS error from mean
    S = errType(dataSet)
    bestS = np.inf; bestIndex = 0; bestValue = 0
    for featIndex in range(n-1):
        for splitVal in dataSet[:,featIndex]:
            mat0, mat1 = binSplitDataSet(dataSet, featIndex, splitVal)
            print mat0.shape
            print mat1.shape
            if (np.shape(mat0)[0] < tolN) or (np.shape(mat1)[0] < tolN): continue
            newS = errType(mat0) + errType(mat1)
            if newS < bestS:
                bestIndex = featIndex
                bestValue = splitVal
                bestS = newS
    #if the decrease (S-bestS) is less than a threshold don't do the split
    if (S - bestS) < tolS:
        return None, leafType(dataSet) #exit cond 2
    mat0, mat1 = binSplitDataSet(dataSet, bestIndex, bestValue)
    if (np.shape(mat0)[0] < tolN) or (np.shape(mat1)[0] < tolN):  #exit cond 3
        return None, leafType(dataSet)
    return bestIndex,bestValue#returns the best feature to split on
                              #and the value used for that split
def createTree(dataSet, leafType=regLeaf, errType=regErr, ops=(1,4)):#assume dataSet is NumPy Mat so we can array filtering
    #print dataSet.shape
    feat, val = chooseBestSplit(dataSet, leafType, errType, ops)#choose the best split
    if feat == None: return val #if the splitting hit a stop condition return val
    retTree = {}
    retTree['spInd'] = feat
    retTree['spVal'] = val
    lSet, rSet = binSplitDataSet(dataSet, feat, val)
    print lSet.shape
    print rSet.shape
    retTree['left'] = createTree(lSet, leafType, errType, ops)
    retTree['right'] = createTree(rSet, leafType, errType, ops)
    return retTree
if __name__ == '__main__':
    myDat = loadDataSet('ex00.txt')
    myDat = np.mat(myDat)
    print myDat.shape
    createTree(myDat)
