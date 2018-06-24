#!/usr/bin/python3
'''
by yaung(yaungwaung@163.com) on 20171128
test on bash for win10, ubuntu 16.04
'''
import sys
import datetime
from sudoku import *

def cal(source):
    n = len([i for i in source if i in '1234356789'])
    print('%s (%d) -> ' % (source.strip('\n'), n), end='')
    t_s = datetime.datetime.now()
    sys.stdout.flush()
    for r in sudoku_cal(source):
        print(r, end='')
        break
    t_e = datetime.datetime.now()
    t = t_e - t_s
    print(' : %d.%d' % (t.seconds, t.microseconds))

source_file = './source'
with open(source_file) as f:
    sources = f.readlines()

n = 1
num = len(sources)
for source in sources:
    if len(source) >= 81:
        print('%s/%s ' % (n, num), end='')
        cal(source)
        n += 1
