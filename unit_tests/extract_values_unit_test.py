__author__ = 'Grega'

import unittest
import SAT_implementation.bool_formulas as bf
import SAT_implementation.algorithm_utilities as au


class extract_values_unit_test(unittest.TestCase):
	"""
	Unit test for the extract values method of the algorithm utilities.
	"""

	def test_simple_extraction_of_values(self):
		"""
		Tests extracting values from a simple formula. Result must be [a, b].
		"""
		self.assertEqual(["a", "b"], au.extract_variables(bf.And([bf.Var("b"), bf.Var("a")])), "Invalid variables extracted, expected [a, b].")

	def test_complex_extraction_of_values(self):
		"""
		Tests extracting values from a simple formula. Result must be [a, b, c].
		"""
		a = bf.Var("a")
		b = bf.Var("b")
		c = bf.Var("c")
		formula = bf.And([bf.Or([b, a, c]), bf.Or([bf.Not(a), bf.Not(c)]), bf.Not(b)])
		self.assertEqual(["a", "b", "c"], au.extract_variables(formula), "Invalid variables extracted, expected [a, b, c].")

	def test_extracting_one_value(self):
		"""
		Tests extracting values where only one value is present. Result must be [b].
		"""
		self.assertEqual(["b"], au.extract_variables(bf.Var("b")), "Invalid variables extracted, expected [b].")

	def test_extracting_no_values(self):
		"""
		Tests extracting values where no values are present. Result must be empty list ([]).
		"""
		formula = bf.And([bf.Or([bf.Tru(), bf.Tru(), bf.Tru()]), bf.Or([bf.Not(bf.Tru()), bf.Not(bf.Tru())]), bf.Not(bf.Tru())])
		self.assertEqual([], au.extract_variables(formula), "Invalid variables extracted, expected [].")

if __name__ == '__main__':
	"""
	Runs the unit test if the script is run directly.
	"""
	unittest.main()

