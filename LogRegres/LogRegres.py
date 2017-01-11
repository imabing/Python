# -*- coding:utf-8 -*-
import numpy as np
def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat
def sigmoid(inX):
    return 1.0/(1+np.exp(-inX))
def gradAscent(dataMatIn,classLabels):
    dataMatrix = np.mat(dataMatIn)
    labelMat = np.mat(classLabels).transpose()
    m,n = np.shape(dataMatrix)
    alpha = 0.001                #梯度下降步长
    maxCycles = 500              #迭代次数
    weights = np.ones((n,1))     #权重w0,w1
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)
        error = labelMat - h
        weights = weights + alpha*dataMatrix.transpose()*error
    return weights
def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat,labelMat=loadDataSet()
    dataArr = np.array(dataMat)
    n = np.shape(dataArr)[0]       #100行数据
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,0]); ycord1.append(dataArr[i,1])
        else:
            xcord2.append(dataArr[i,0]); ycord2.append(dataArr[i,1])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = np.arange(-3.0, 3.0, 0.1)  #x为numpy.arange格式，并且以0.1为步长从-3.0到3.0切分。
    # 拟合曲线为0 = w0*x0+w1*x1+w2*x2, 故x2 = (-w0*x0-w1*x1)/w2, x0为1,x1为x, x2为y,故有
    #y = (-weights[0]-weights[1]*x)/weights[2]
    y = (-1 - weights[0] * x) / weights[1]
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.show()
if __name__ == '__main__':
    dataMat,labelMat = loadDataSet()
    weights = gradAscent(dataMat,labelMat)
    print weights
    plotBestFit(weights.getA())   #weights为matrix格式，故需要调用getA()方法，其将matrix()格式矩阵转为array()格式