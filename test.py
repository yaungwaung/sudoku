#!/usr/bin/python3
'''
by yaung(yaungwaung@163.com) on 20171207
test on bash for win10, ubuntu 16.04
'''
import sudoku
import unittest

ss = ['005300000800000020070010500400005300010070006003200080060500009004000030000009700',
      '145327698839654127672918543496185372218473956753296481367542819984761235521839764']

class sudoku_test(unittest.TestCase):
    def test(self):
        '''test full feature sudoku calculater'''
        s = sudoku.sudoku_cal(ss[0])
        self.assertEqual(ss[1], next(s))

    def test1(self):
        '''test easy sudoku calculater'''
        s = sudoku.sudoku_cal(ss[0], False)
        self.assertEqual(ss[1], next(s))

if __name__ == '__main__':
    unittest.main()
