# -*- coding:utf-8 -*-
import re   #正则语言模块（re）和collections模块
from collections import Counter
# 1.定义words()函数，用来取出文本库的每一个词。
def words(text): return re.findall(r'\w+', text.lower())
#2.统计词语在文本库的出现频率键值结构
Dictionariy = Counter(words(open('big.txt').read()))
#3.统计一个词在词典中的概率
def P(word, N=sum(Dictionariy.values())):
    return Dictionariy[word] / N
def correction(word):
    return max(candidates(word), key=P)
def candidates(word):
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])
def known(words):
    return set(w for w in words if w in Dictionariy)
def edits1(word):
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]    #'abc'=>[('', 'abc'), ('a', 'bc'), ('ab', 'c'), ('abc', '')]
    deletes    = [L + R[1:]               for L, R in splits if R]          #'abc'=>['bc', 'ac', 'ab'] 。
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]   #'abc' => ['bac', 'acb']
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters] #'abc'=> ['abc', 'bbc', 'cbc', ... , 'abx', ' aby', 'abz' ]  26*3个
    inserts    = [L + c + R               for L, R in splits for c in letters] #'abc' =>['aabc', 'babc', 'cabc', ..., 'abcx', 'abcy', 'abcz']，一共包含104个词（26 × 4）。
    return set(deletes + transposes + replaces + inserts)
def edits2(word):
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
if __name__ == '__main__':
    word = 'deskw'
    # print correction(word)
    # print sum(Dictionariy.values())
    print edits1(word)