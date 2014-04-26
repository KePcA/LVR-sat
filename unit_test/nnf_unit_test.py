from SAT_implementation import bool_formulas as bf

__author__ = 'Grega'

import unittest
import SAT_implementation.algorithm_utilities as au


class nnf_unit_test(unittest.TestCase):

	def test_formulas_already_in_nnf(self):
		formula = bf.Or([bf.And([bf.Var("a"), bf.Var("b")]), bf.Var("c")])
		self.assertEqual(formula, au.nnf(formula))

		formula = bf.And([bf.Or([bf.Var("a"), bf.Var("b")]), bf.Var("c")])
		self.assertEqual(formula, au.nnf(formula))

		formula = bf.And([bf.Var("a"), bf.Or([bf.Var("b"), bf.And([bf.Var("c"), bf.Var("d")])])])
		self.assertEqual(formula, au.nnf(formula))

		formula = bf.Or([bf.Var("a"), bf.Not(bf.Var("b"))])
		self.assertEqual(formula, au.nnf(formula))

		formula = bf.And([bf.Var("a"), bf.Not(bf.Var("b"))])
		self.assertEqual(formula, au.nnf(formula))

		formula = bf.And([bf.Var("a"), bf.Not(bf.Var("b"))])
		self.assertEqual(formula, au.nnf(formula))

		formula = bf.Or([bf.And([bf.Var("a"), bf.Or([bf.Not(bf.Var("b")), bf.Var("c")]), bf.Not(bf.Var("b"))]), bf.Var("d")])
		self.assertEqual(formula, au.nnf(formula))

		formula = bf.And([bf.Var("a"), bf.Or([bf.Var("b"), bf.Not(bf.Var("c"))])])
		self.assertEqual(formula, au.nnf(formula))

		formula = bf.Or([bf.And([bf.Var("a"), bf.Var("b")]), bf.And([bf.Var("a"), bf.Not(bf.Var("c"))])])
		self.assertEqual(formula, au.nnf(formula))

	def test_conversion_to_cnf(self):
		formula = bf.Not(bf.Or([bf.Var("a"), bf.Var("b")]))
		result = bf.And([bf.Not(bf.Var("a")), bf.Not(bf.Var("b"))])
		self.assertEqual(result, au.nnf(formula))

		formula = bf.Not(bf.And([bf.Var("a"), bf.Var("b")]))
		result = bf.Or([bf.Not(bf.Var("a")), bf.Not(bf.Var("b"))])
		self.assertEqual(result, au.nnf(formula))

		formula = bf.Not(bf.And([bf.Var("a"), bf.Not(bf.Var("b"))]))
		result = bf.Or([bf.Not(bf.Var("a")), bf.Var("b")])
		self.assertEqual(result, au.nnf(formula))

if __name__ == '__main__':
	unittest.main()