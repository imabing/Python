# -*- coding: gbk -*-
import numpy as np
def fileToMatrix(fileName):
    fr=open(fileName)
    arrayOfLines=fr.readlines()
    # numOfLines=len(arrayOfLines)
    labels=[]
    for line in arrayOfLines:
        # ȥ��β������\n
        line=line.strip()
        if line:
           labels.append(line)
    return labels

if __name__ == '__main__':
    labels=fileToMatrix('G:\\����\\���ϱ���\\΢��\\2016-2.txt')
    for item in labels:
        print item
    print 'Total Record:'+str(len(labels))
