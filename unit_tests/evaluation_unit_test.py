__author__ = 'Grega'

import unittest
import SAT_implementation.bool_formulas as bf

class evaluation_unit_test(unittest.TestCase):
	"""
	Unit test for the evaluation method of the algorithm utilities.
	"""

	def test_simple_evaluation_to_true(self):
		"""
		Tests the evaluation of a simple formula with the specified values. Must evaluate to True.
		"""
		values = {"a": bf.Tru(), "b": bf.Fls(), "c": bf.Fls()}
		formula = bf.And([bf.Or([bf.Var("b"), bf.Var("a"), bf.Var("c")]), bf.Or([bf.Not(bf.Var("a")), bf.Not(bf.Var("c"))]), bf.Not(bf.Var("b"))])
		result = formula.evaluate(values)

		self.assertTrue(result, "Invalid evaluation, expected True.")

	def test_simple_evaluation_to_false(self):
		"""
		Tests the evaluation of a simple formula with the specified values. Must evaluate to False.
		"""
		values = {"a": bf.Fls(), "b": bf.Fls(), "c": bf.Fls()}
		formula = bf.And([bf.Or([bf.Var("b"), bf.Var("a"), bf.Var("c")]), bf.Or([bf.Not(bf.Var("a")), bf.Not(bf.Var("c"))]), bf.Not(bf.Var("b"))])
		result = formula.evaluate(values)

		self.assertFalse(result, "Invalid evaluation, expected False.")

	def test_complex_evaluation_to_true(self):
		"""
		Tests the evaluation of a complex formula with the specified values. Must evaluate to True.
		"""
		values = {"a": bf.Fls(), "b": bf.Fls(), "c": bf.Fls()}
		formula = bf.And([bf.Not(bf.Var("a")), bf.Or([bf.And([bf.Var("a"), bf.Var("b"), bf.Var("c")]), bf.Not(bf.Var("b"))])])
		result = formula.evaluate(values)

		self.assertTrue(result, "Invalid evaluation, expected True.")

	def test_complex_evaluation_to_false(self):
		"""
		Tests the evaluation of a complex formula with the specified values. Must evaluate to False.
		"""
		values = {"a": bf.Tru(), "b": bf.Tru(), "c": bf.Fls()}
		formula = bf.And([bf.Not(bf.Var("a")), bf.Or([bf.And([bf.Var("a"), bf.Var("b"), bf.Var("c")]), bf.Not(bf.Var("b"))])])
		result = formula.evaluate(values)

		self.assertFalse(result, "Invalid evaluation, expected False.")


if __name__ == '__main__':
	"""
	Runs the unit test if the script is run directly.
	"""
	unittest.main()
