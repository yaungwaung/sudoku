#!/usr/bin/python3
'''
by yaung(yaungwaung@163.com) on 20171202
test on bash for win10, ubuntu 16.04
'''
__author__ = 'yaung'

import re

need_check = lambda i, j : i//9 == j//9 or i%9 == j%9 or (i//9//3 == j//9//3 and i%9//3 == j%9//3)
check_index = lambda i : [j for j in range(81) if need_check(i, j) and i != j]
legal_check = lambda sudoku, i : sudoku[i] not in [sudoku[j] for j in check_index(i)]

def sudoku_cal_simple(nums):
    '''Simple sudoku calculater.

    it's very short.
    it takes a little long to find answers.
    it won't verify wrong input.'''
    sudoku = [int(i) for i in ''.join(re.findall('\d', nums)).ljust(81, '0')[:81]]
    cache = []
    while True:
        if not cache or legal_check(sudoku, cache[-1]):
            if sudoku.count(0) == 0:
                yield ''.join([str(i) for i in sudoku])
            else:
                cache.append(sudoku.index(0))
                sudoku[cache[-1]] = 1
                continue

        while cache and sudoku[cache[-1]] == 9:
            sudoku[cache[-1]] = 0
            cache.pop()

        if not cache:
            break

        sudoku[cache[-1]] += 1

def clear_sudoku(sudoku):
    flag = True
    while flag:
        flag = False

        for i in (i for i in range(81) if len(sudoku[i]) == 1):
            if any(sudoku[i] == sudoku[k] for k in check_index(i)):
                return -1
            for k in (k for k in check_index(i) if sudoku[i] in sudoku[k]):
                sudoku[k] = sudoku[k].replace(sudoku[i], '')
                flag = True

        #for i in [i for i in range(81) if len(sudoku[i]) > 1]:
        #    nums = ''.join([sudoku[k] for k in check_index(i)])
        #    poss = [str(m) for m in range(1, 10) if str(m) not in nums]
        #    if len(poss) > 1:
        #        return -1
        #    if len(poss) == 1:
        #        sudoku[i] = poss[0]
        #        flag = True

    return len([i for i in range(81) if len(sudoku[i]) > 1])

def sudoku_cal_full(nums):
    '''Full features sudoku calculater.

    it returns all answers.
    it's a little quicker than sudoku_cal_simple.
    it can verify the input legarity.'''
    sudoku = [i.replace('0', '123456789') for i in ''.join(re.findall('\d', nums)).ljust(81, '0')[:81]]
    cache = []
    while True:
        unsure_c = clear_sudoku(sudoku)
        
        if unsure_c == 0:
            yield ''.join(sudoku)

        if unsure_c > 0:
            i = [i for i in range(81) if len(sudoku[i]) > 1][0]
            cache.append([sudoku.copy(), i, 0])
            sudoku[i] = sudoku[i][0]
            continue

        while cache and len(cache[-1][0][cache[-1][1]]) == cache[-1][2] + 1:
            cache.pop()

        if not cache:
            break

        sudoku, i, n = cache[-1]
        sudoku = sudoku.copy()
        sudoku[i] = sudoku[i][n + 1]
        cache[-1][2] = n + 1
        
def sudoku_cal(nums, full=True):
    ''' Sudoku calculater.

    default option "full" means use full feature calculater.'''
    if full:
        return sudoku_cal_full(nums)
    else:
        return sudoku_cal_simple(nums)

if __name__ == '__main__':
    source = '005300000800000020070010500400005300010070006003200080060500009004000030000009700'
    #source = '145327698839654127672918543496185372218473956753296481367542819984761235521839764'
    #source = '145327698839654127672918543496185372218473956753296481367542819984761235521839765'
    #source = '1453276988396541276729185434961853722184739567532964813675428'
    #source = '800000000003600000070090200050007000000045700000100030001000068008500010090000400'
    #for r in sudoku_cal(source, False):
    for r in sudoku_cal(source):
        print(r)
