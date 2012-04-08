#coding: utf-8
import sys
import os
import re
import random
FILE_NAME = 'deutsch_sprache.txt'

words = []
yes = []
no = []

def run(filename):
    reobj = re.compile("[^\u4e00-\u9fa5\.\?\!]+")
    lines = open(filename).readlines()
    for x in lines:
        if len(x) > 3:
            result = reobj.findall(unicode(x, 'utf-8'))
            for y in result:
                if len(y) > 4:
                    st_str = y
                    break

            pos = unicode(x,'utf-8').find(st_str)
            words.append({'de':x[:pos],'ch':x[pos:]})

    ll = len(words)
    while True:
        while True:
            r = random.randint(0,ll-1)
            if r not in yes:
                break
        print words[r]['de']
        t = input('1:会了，2:不会, 3:复习:')
        print words[r]['ch']

        print t
        if t == 1:
            yes.append(r)
        elif t == 2:
            no.append(r)
        elif t == 3:
            break

    for x in no:
        print words[r]['de']
        t = input('1:会了, 2:不会')
        print words[r]['ch']

        if t == 2:
            no.append(x)



            

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        run(FILE_NAME)

