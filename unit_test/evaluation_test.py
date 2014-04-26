from SAT_implementation import bool_formulas as bf

__author__ = 'Grega'

import unittest


class evaluation_unit_test(unittest.TestCase):

	def test_evaluating(self):
		q = bf.Var("q")
		p = bf.Var("p")
		r = bf.Var("r")
		values = {"p": bf.Tru(), "q": bf.Fls(), "r": bf.Fls()}
		formula = bf.And([bf.Or([q, p, r]), bf.Or([bf.Not(p), bf.Not(r)]), bf.Not(q)])
		result = formula.evaluate(values)

		self.assertTrue(result)

if __name__ == '__main__':
	unittest.main()
