# -*- coding:utf-8 -*-
from Tree import *
import pickle
def storeTree(inputTree, filename):
    fw = open(filename)
    pickle.dump(inputTree, fw)
    fw.close()
def grabTree(filename):
    fr = open(filename)
    return pickle.load(fr)
if __name__ == '__main__':
    fr = open('lenses.txt')
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
    lensesTree = createTree(lenses, lensesLabels)
    # print lensesTree
    # storeTree(lensesTree, 'treed.txt')
    # print grabTree('lenses.txt')