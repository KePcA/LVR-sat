__author__ = 'Grega'

import unittest
import SAT_implementation.bool_formulas as bf
import SAT_implementation.algorithm_utilities as au


class nnf_unit_test(unittest.TestCase):
	"""
	Unit test for the nnf method of the algorithm utilities.
	"""

	def test_formulas_already_in_nnf(self):
		"""
		Tests the conversion of formulas that are already in nnf form.
		"""
		formula = bf.Or([bf.And([bf.Var("a"), bf.Var("b")]), bf.Var("c")])
		self.assertEqual(formula, au.nnf(formula), "Invalid formula, expected the same as entered.")

		formula = bf.And([bf.Or([bf.Var("a"), bf.Var("b")]), bf.Var("c")])
		self.assertEqual(formula, au.nnf(formula), "Invalid formula, expected the same as entered.")

		formula = bf.And([bf.Var("a"), bf.Or([bf.Var("b"), bf.And([bf.Var("c"), bf.Var("d")])])])
		self.assertEqual(formula, au.nnf(formula), "Invalid formula, expected the same as entered.")

		formula = bf.Or([bf.Var("a"), bf.Not(bf.Var("b"))])
		self.assertEqual(formula, au.nnf(formula), "Invalid formula, expected the same as entered.")

		formula = bf.And([bf.Var("a"), bf.Not(bf.Var("b"))])
		self.assertEqual(formula, au.nnf(formula), "Invalid formula, expected the same as entered.")

		formula = bf.And([bf.Var("a"), bf.Not(bf.Var("b"))])
		self.assertEqual(formula, au.nnf(formula), "Invalid formula, expected the same as entered.")

		formula = bf.Or([bf.And([bf.Var("a"), bf.Or([bf.Not(bf.Var("b")), bf.Var("c")]), bf.Not(bf.Var("b"))]), bf.Var("d")])
		self.assertEqual(formula, au.nnf(formula), "Invalid formula, expected the same as entered.")

		formula = bf.And([bf.Var("a"), bf.Or([bf.Var("b"), bf.Not(bf.Var("c"))])])
		self.assertEqual(formula, au.nnf(formula), "Invalid formula, expected the same as entered.")

		formula = bf.Or([bf.And([bf.Var("a"), bf.Var("b")]), bf.And([bf.Var("a"), bf.Not(bf.Var("c"))])])
		self.assertEqual(formula, au.nnf(formula), "Invalid formula, expected the same as entered.")

	def test_simple_conversion_to_nnf(self):
		"""
		Tests the conversion of simple formulas that aren't in nnf yet.
		"""
		formula = bf.Not(bf.Or([bf.Var("a"), bf.Var("b")]))
		result = bf.And([bf.Not(bf.Var("a")), bf.Not(bf.Var("b"))])
		self.assertEqual(result, au.nnf(formula), "Invalid formula, expected the same as specified by result.")

		formula = bf.Not(bf.And([bf.Var("a"), bf.Var("b")]))
		result = bf.Or([bf.Not(bf.Var("a")), bf.Not(bf.Var("b"))])
		self.assertEqual(result, au.nnf(formula), "Invalid formula, expected the same as specified by result.")

		formula = bf.Not(bf.And([bf.Var("a"), bf.Not(bf.Var("b"))]))
		result = bf.Or([bf.Not(bf.Var("a")), bf.Var("b")])
		self.assertEqual(result, au.nnf(formula), "Invalid formula, expected the same as specified by result.")

	def test_complex_conversion_to_nnf(self):
		"""
		Tests the conversion of complex formulas that aren't in nnf yet.
		"""
		formula = bf.And([bf.Var("a"), bf.And([bf.Var("b"), bf.Var("a")]), bf.Or([bf.Var("c"), bf.Var("b")])])
		result = bf.And([bf.Var("a"), bf.And([bf.Var("b"), bf.Var("a")]), bf.Or([bf.Var("c"), bf.Var("b")])])
		self.assertEqual(result, au.nnf(formula), "Invalid formula, expected the same as specified by result.")

		formula = bf.And([bf.Not(bf.Var("a")), bf.Or([bf.And([bf.Var("a"), bf.Var("b"), bf.Var("c")]), bf.Not(bf.Var("b"))])])
		result = bf.And([bf.Not(bf.Var("a")), bf.Or([bf.And([bf.Var("a"), bf.Var("b"), bf.Var("c")]), bf.Not(bf.Var("b"))])])
		self.assertEqual(result, au.nnf(formula), "Invalid formula, expected the same as specified by result.")

		formula = bf.And([bf.Not(bf.Var("a")),bf.Or([bf.And([bf.Var("b"), bf.Var("c"), bf.Var("d")]), bf.Not(bf.Var("c"))]), bf.Var("a")])
		result = bf.And([bf.Not(bf.Var("a")),bf.Or([bf.And([bf.Var("b"), bf.Var("c"), bf.Var("d")]), bf.Not(bf.Var("c"))]), bf.Var("a")])
		self.assertEqual(result, au.nnf(formula), "Invalid formula, expected the same as specified by result.")

if __name__ == '__main__':
	"""
	Runs the unit test if the script is run directly.
	"""
	unittest.main()