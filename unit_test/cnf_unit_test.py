__author__ = 'Grega'

import unittest
import bool_formulas as bf
import SAT_implementation.algorithm_utilities as au

class cnf_unit_test(unittest.TestCase):

	def test_formulas_already_in_cnf(self):
		formula = bf.And([bf.Not(bf.Var("a")), bf.Or([bf.Var("b"), bf.Var("c")])])
		self.assertEqual(formula, au.cnf_nnf(formula))

		formula = bf.And([bf.Var("a"), bf.Var("b")])
		self.assertEqual(formula, au.cnf_nnf(formula))

		formula = bf.Or([bf.Var("a"), bf.Var("b")])
		self.assertEqual(formula, au.cnf_nnf(formula))

		formula = bf.And([bf.Or([bf.Var("a"), bf.Var("b")]), bf.Or([bf.Not(bf.Var("b")), bf.Var("c"), bf.Not(bf.Var("d"))]), bf.Or([bf.Var("d"), bf.Not(bf.Var("e"))])])
		self.assertEqual(formula, au.cnf_nnf(formula))

	def test_conversion_to_cnf(self):
		formula = bf.Not(bf.Or([bf.Var("a"), bf.Var("b")]))
		result = bf.And([bf.Not(bf.Var("a")), bf.Not(bf.Var("b"))])
		self.assertEqual(result, au.cnf_nnf(formula))

		formula = bf.Or([bf.And([bf.Var("a"), bf.Var("b")]), bf.Var("c")])
		result = bf.And([bf.Or([bf.Var("a"), bf.Var("c")]), bf.Or([bf.Var("b"), bf.Var("c")])])
		self.assertEqual(result, au.cnf_nnf(formula))

		formula = bf.And([bf.Var("a"), bf.Or([bf.Var("b"), bf.And([bf.Var("c"), bf.Var("d")])])])
		result = bf.And([bf.Var("a"), bf.Or([bf.Var("c"), bf.Var("b")]),  bf.Or([bf.Var("d"), bf.Var("b")])])
		self.assertEqual(result, au.cnf_nnf(formula))

if __name__ == '__main__':
	unittest.main()