# -*- coding: gbk -*-
import numpy as np
def fileToMatrix(fileName):
    fr=open(fileName)
    arrayOfLines=fr.readlines()
    # numOfLines=len(arrayOfLines)
    labels=[]
    for line in arrayOfLines:
        # 去除尾部换行\n
        line=line.strip()
        if line:
           labels.append(line)
    return labels

if __name__ == '__main__':
    labels=fileToMatrix('G:\\资料\\资料备份\\微语\\2016-2.txt')
    for item in labels:
        print item
    print 'Total Record:'+str(len(labels))
