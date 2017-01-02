# -*- coding: cp936 -*-
import numpy as np
import matplotlib.pyplot as plt
import operator
def createDataSet():
    data=np.array([[1,1],[2,2],[10,10],[11,11]])
    labels=['A','A','B','B']
    return data,labels
def knn(point,data,labels,k):
    # 数据集行数
    dataSize=data.shape[0]
    # tile复制数组，b = tile(a,(m,n)):即是把a数组里面的元素复制n次放进一个数组c中，然后再把数组c复制m次放进一个数组b中
    subMatrix=np.tile(point,(dataSize,1))-data
    matrixSq=subMatrix**2
    distance=(matrixSq.sum(axis=1))**0.5
    # 升序排列样本索引如： [2 3 1 0]
    sortDistanceIndex=distance.argsort()
    # 取距离最短的k个点
    selectK={}
    for i in range(k):
        kLabel = labels[sortDistanceIndex[i]]
        selectK[kLabel] = selectK.get(kLabel,0) + 1
    sortedSelectK = sorted(selectK.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedSelectK[0][0]
if __name__ == '__main__':
    data,labels=createDataSet()
    print knn([10, 9], data, labels,3)
    # plt.plot(data,'*')
    plt.plot([1,2,10,11],[1,2,10,11], '*')
    plt.plot(10,9,'ro')
    plt.axis([0,12, 0, 12])
    plt.show()

