#coding: utf-8
import sys
import os
import re
import random

from remember import RememberMode

class Startup(object):
    def __init__(self):
        pass


    def loop(self):
        while True:
            print "欢迎使用!"
            ch = input(
            '''
            1: 开始背单词
            2: 录入单词
            3: 退出 
'''
            )
            if ch == 1:
                l = RememberMode()
                l.loop()
                
            elif ch == 2:
                break
            elif ch == 3:
                break
            else:
                print '命令不对'

if __name__ == "__main__":
    p = Startup()
    p.loop()
    
