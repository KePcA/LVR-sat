__author__ = 'Grega'

import unittest
import bool_formulas as bf


class replace_unit_test(unittest.TestCase):

	def test_replacing_one_value(self):
		q = bf.Var("q")
		p = bf.Var("p")
		r = bf.Var("r")
		values = {"p": bf.Tru()}
		formula = bf.And([bf.Or([q, p, r]), bf.Or([bf.Not(p), bf.Not(r)]), bf.Or([bf.Not(q)])])

		self.assertEqual(bf.And([bf.Or([q, bf.Tru(), r]), bf.Or([bf.Not(bf.Tru()), bf.Not(r)]), bf.Or([bf.Not(q)])]), formula.replace(values))

	def test_replacing_all_values(self):
		q = bf.Var("q")
		p = bf.Var("p")
		r = bf.Var("r")
		values = {"q": bf.Tru(), "p": bf.Fls(), "r": bf.Tru()}
		formula = bf.Not(bf.Or([bf.And([bf.Not(q), p, r]), bf.Not(bf.Or([q, bf.Not(p), bf.Tru()]))]))
		self.assertEqual(bf.Not(bf.Or([bf.And([bf.Not(bf.Tru()), bf.Fls(), bf.Tru()]), bf.Not(bf.Or([bf.Tru(), bf.Not(bf.Fls()), bf.Tru()]))])), formula.replace(values))

if __name__ == '__main__':
	unittest.main()
