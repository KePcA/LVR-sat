__author__ = 'Grega'

import unittest
import SAT_implementation.bool_formulas as bf
import SAT_implementation.algorithm_utilities as au


class cnf_unit_test(unittest.TestCase):
	"""
	Unit test for the cnf_nnf method of the algorithm utilities.
	"""

	def test_formulas_already_in_cnf(self):
		"""
		Tests the conversion of formulas that are already in cnf form.
		"""
		formula = bf.And([bf.Not(bf.Var("a")), bf.Or([bf.Var("b"), bf.Var("c")])])
		self.assertEqual(formula, au.cnf_nnf(formula), "Invalid formula, expected the same as entered.")

		formula = bf.And([bf.Var("a"), bf.Var("b")])
		self.assertEqual(formula, au.cnf_nnf(formula), "Invalid formula, expected the same as entered.")

		formula = bf.Or([bf.Var("a"), bf.Var("b")])
		self.assertEqual(formula, au.cnf_nnf(formula), "Invalid formula, expected the same as entered.")

		formula = bf.And([bf.Or([bf.Var("a"), bf.Var("b")]), bf.Or([bf.Not(bf.Var("b")), bf.Var("c"), bf.Not(bf.Var("d"))]), bf.Or([bf.Var("d"), bf.Not(bf.Var("e"))])])
		self.assertEqual(formula, au.cnf_nnf(formula), "Invalid formula, expected the same as entered.")

	def test_conversion_to_cnf(self):
		"""
		Tests the conversion of formulas that aren't in cnf form.
		"""
		formula = bf.Not(bf.Or([bf.Var("a"), bf.Var("b")]))
		result = bf.And([bf.Not(bf.Var("a")), bf.Not(bf.Var("b"))])
		self.assertEqual(result, au.cnf_nnf(formula), "Invalid formula, expected the same as specified by result.")

		formula = bf.Or([bf.And([bf.Var("a"), bf.Var("b")]), bf.Var("c")])
		result = bf.And([bf.Or([bf.Var("a"), bf.Var("c")]), bf.Or([bf.Var("b"), bf.Var("c")])])
		self.assertEqual(result, au.cnf_nnf(formula), "Invalid formula, expected the same as specified by result.")

		formula = bf.And([bf.Var("a"), bf.Or([bf.Var("b"), bf.And([bf.Var("c"), bf.Var("d")])])])
		result = bf.And([bf.Var("a"), bf.Or([bf.Var("c"), bf.Var("b")]),  bf.Or([bf.Var("d"), bf.Var("b")])])
		self.assertEqual(result, au.cnf_nnf(formula), "Invalid formula, expected the same as specified by result.")

	def test_conversion_to_cnf_with_true_in_or(self):
		"""
		Tests the conversion of formula that isn't in cnf form and contains a True in a Or formula.
		"""
		formula = bf.Not(bf.And([bf.Var("a"), bf.Var("b"), bf.Not(bf.Tru())]))
		self.assertEqual(bf.Tru(), au.cnf_nnf(formula), "Invalid formula, expected Tru.")

	def test_conversion_to_cnf_with_false_in_and(self):
		"""
		Tests the conversion of formula that isn't in cnf form and contains a False in a And formula.
		"""
		formula = bf.Not(bf.Or([bf.Var("a"), bf.Var("b"), bf.Not(bf.Fls())]))
		self.assertEqual(bf.Fls(), au.cnf_nnf(formula), "Invalid formula, expected Fls.")

if __name__ == '__main__':
	"""
	Runs the unit test if the script is run directly.
	"""
	unittest.main()