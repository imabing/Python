import numpy as np
import operator
def createDataSet():
    data=np.array([[1,1],[1,2],[10,10],[10,11]])
    labels=['A','A','B',b'']
    return data,labels
def knn(point,data,labels,k):
    # 数据集样本数
    dataSize=data.shape[0]

    return dataSize
if __name__ == '__main__':
    data,lables=createDataSet()
    print knn([1,3],data,lables,4)