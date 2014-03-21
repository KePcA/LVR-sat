__author__ = 'Grega'

import unittest
import bool_formulas as bf
import SAT_implementation.algorithm_utilities as au

class replace_unit_test(unittest.TestCase):

	def setUp(self):
		self.seq = range(10)


	def test_replacing_one_value(self):
		q = bf.Var("q")
		p = bf.Var("p")
		r = bf.Var("r")
		values = {"p": bf.Tru()}
		result = au.replace(values, bf.And([bf.Or([q, p, r]), bf.Or([bf.Not(p), bf.Not(r)]), bf.Or([bf.Not(q)])]))

		self.assertEqual(bf.And([bf.Or([q, bf.Tru(), r]), bf.Or([bf.Not(bf.Tru()), bf.Not(r)]), bf.Or([bf.Not(q)])]), result)

	def test_replacing_all_values(self):
		q = bf.Var("q")
		p = bf.Var("p")
		r = bf.Var("r")
		values = {"q": bf.Tru(), "p": bf.Fls(), "r": bf.Tru()}

		result = au.replace(values, bf.Not(bf.Or([bf.And([bf.Not(q), p, r]), bf.Not(bf.Or([q, bf.Not(p), bf.Tru()]))])))
		self.assertEqual(bf.Not(bf.Or([bf.And([bf.Not(bf.Tru()), bf.Fls(), bf.Tru()]), bf.Not(bf.Or([bf.Tru(), bf.Not(bf.Fls()), bf.Tru()]))])), result)

if __name__ == '__main__':
	unittest.main()
