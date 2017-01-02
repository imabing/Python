# -*- coding: cp936 -*-
import numpy as np
import matplotlib.pyplot as plt
import operator
def createDataSet():
    data=np.array([[1,1],[2,2],[10,10],[11,11]])
    labels=['A','A','B','B']
    return data,labels
def knn(point,data,labels,k):
    # ���ݼ�����
    dataSize=data.shape[0]
    # tile�������飬b = tile(a,(m,n)):���ǰ�a���������Ԫ�ظ���n�ηŽ�һ������c�У�Ȼ���ٰ�����c����m�ηŽ�һ������b��
    subMatrix=np.tile(point,(dataSize,1))-data
    matrixSq=subMatrix**2
    distance=(matrixSq.sum(axis=1))**0.5
    # �����������������磺 [2 3 1 0]
    sortDistanceIndex=distance.argsort()
    # ȡ������̵�k����
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

