#coding: utf-8
import sys
import os
import re
import random

class Remember(object):
    def __init__(self):
        self.words = []
        self.yes = []
        self.no = []


    def run(self, filename):
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
                self.words.append({'de':x[:pos],'ch':x[pos:]})

        ll = len(self.words)
        while True:
            while True:
                r = random.randint(0,ll-1)
                if r not in self.yes:
                    break
            print self.words[r]['de']
            t = input('1:会了，2:不会, 3:复习:')
            print self.words[r]['ch']

            if t == 1:
                self.yes.append(r)
            elif t == 2:
                self.no.append(r)
            elif t == 3:
                break

        for x in self.no:
            print self.words[r]['de']
            t = input('1:会了, 2:不会')
            print self.words[r]['ch']

            if t == 2:
                self.no.append(x)


class RememberMode(object):
    def __init__(self):
        self.files = self.get_files()
        self.choice = 0


    def get_files(self):
        res = []
        for x in os.listdir('data/'):
            res.append(os.path.join('data', x))
        return res


    def loop(self):
        while True:
            while True:
                print 0, ': 返回'
                for x in range(len(self.files)):
                    print x+1, ':', self.files[x]
                t = input('请选择单词文件:')
                if t >= 0 and t <= len(self.files):
                    self.choice = t-1
                    break
            if self.choice < 0: #返回
                break
            else: #选择了一个单词文件
                l = Remember()
                l.run(self.files[self.choice])


FILE_NAME = 'deutsch_sprache.txt'

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        run(FILE_NAME)

