__author__ = 'Grega'

import random
import unittest
import bool_formulas as bf
import SAT_implementation.algorithm_utilities as au

class replace_unit_test(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)


    def test_shuffle(self):
        q = bf.Var("q")
        p = bf.Var("p")
        r = bf.Var("r")
        values = {"p" : bf.Tru()}
        a = au.replace(values, bf.And([bf.Or([q,p, r]), bf.Or([bf.Not(p), bf.Not(r)]), bf.Or([bf.Not(q)])]))
        print a


if __name__ == '__main__':
    unittest.main()
