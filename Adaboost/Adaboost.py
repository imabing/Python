import numpy as np
from numpy import ones
def loadSimData():
    datMat = np.matrix([[1.0, 2.1],
                        [2.0, 1.1],
                        [1.3, 1.0],
                        [1.0, 1.0],
                        [2.0, 1.0]])
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return datMat, classLabels
#根据阈值进行分类，左边为-1，右边为1
def stumpClassify(datMatrix, dimen, threshval, threshIneq): #dimen维度：X维or Y维；threshval阈值；threshIneq左边取1还是右边取1
    retArray = np.ones((np.shape(datMatrix)[0], 1))
    if threshIneq == 'lt':
        retArray[datMatrix[:, dimen] <= threshval] = -1.0
    else:
        retArray[datMatrix[:, dimen] > threshval] = -1.0
    return retArray
#单层决策树生成函数
def buildStump(dataArr, classLabels, D):
    dataMatrix = np.mat(dataArr)
    labelMat = np.mat(classLabels).T
    m, n = np.shape(dataMatrix)
    numSteps = 10.0
    bestStump = {}
    bestClassEst = np.mat(np.zeros((m, 1)))
    minError = np.inf
    for i in range(n):
        rangeMin = dataMatrix[:, i].min()
        rangeMax = dataMatrix[:, i].max()
        stepSize = (rangeMax - rangeMin) / numSteps
        for j in range(-1, int(numSteps) + 1):
            for inequal in ['lt', 'gt']:
                threshval = (rangeMin + float(j) * stepSize)
                predictedVals = stumpClassify(dataMatrix, i, threshval, inequal)
                errArr = np.mat(np.ones((m, 1)))
                errArr[predictedVals == labelMat] = 0
                weightArr = D.T * errArr
                if weightArr < minError:
                    minError = weightArr
                    bestClassEst = predictedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshval
                    bestStump['ineq'] = inequal
    return bestStump, minError, bestClassEst

def adaBoostTrainDs(dataArr, classLabels, numIt=40):
    werkClassArr = []
    m = np.shape(dataArr)[0]
    D = np.mat(np.ones((m, 1)) / m)
    aggClassEst = np.mat(np.zeros((m, 1)))
    for i in range(numIt):
        bestStump, error, classEst = buildStump(datMat, classLabels, D)
        print 'D:', D.T

        alpha = float(0.5 * np.log((1.0 - error) / np.max(error, 1e-16)))
        bestStump['alpha'] = alpha
        werkClassArr.append(bestStump)

        print 'classEst', classEst

        expon = np.multiply(-1 * alpha * np.mat(classLabels).T, classEst)
        D = np.multiply(D, np.exp(expon))
        D = D / D.sum()
        aggClassEst += alpha * classEst

        print 'aggClassEst', aggClassEst.T

        aggErrors = np.multiply(np.sign(aggClassEst) != np.mat(classLabels).T, np.ones((m, 1)))
        errorRate = aggErrors.sum() / m
        print 'total error:', errorRate
        if errorRate == 0.0:
            break
    return werkClassArr


if __name__ == '__main__':
    D = np.mat(np.ones((5, 1)) / 5)
    datMat, classLabels = loadSimData()
    bestStump, minError, bestClassEst = buildStump(datMat, classLabels, D)
    adaBoostTrainDs(datMat, classLabels, 10)