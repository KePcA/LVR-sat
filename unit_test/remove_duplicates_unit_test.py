__author__ = 'Grega'

import unittest
import SAT_implementation.bool_formulas as bf
import SAT_implementation.algorithm_utilities as au


class remove_duplicates_unit_test(unittest.TestCase):
	"""
	Unit test for the removing duplicates method of the algorithm utilities.
	"""

	def test_with_empty_list(self):
		"""
		Test removing duplicates from an empty list. Result must be empty list ([]).
		"""
		self.assertEqual([], au.remove_duplicates([]), "Invalid removal, expected [].")

	def test_with_duplicates(self):
		"""
		Test removing duplicates. Result must be duplicates removed.
		"""
		formula = [bf.Var("b"), bf.Var("a"), bf.Var("b"), bf.Var("c"), bf.Var("a"), bf.Tru(), bf.Fls(), bf.Var("c")]
		result = [bf.Fls(), bf.Tru(), bf.Var("a"), bf.Var("b"), bf.Var("c")]
		self.assertEqual(result, au.remove_duplicates(formula), "Invalid replacement, expected the same as specified by result.")

	def test_with_no_duplicates(self):
		"""
		Test removing values that do not contain duplicates. Result must be the same as the input.
		"""
		formula = [bf.Var("b"), bf.Var("a")]
		result = [bf.Var("a"), bf.Var("b")]
		self.assertEqual(result, au.remove_duplicates(formula), "Invalid removal, expected the same as specified by result.")

if __name__ == '__main__':
	"""
	Runs the unit test if the script is run directly.
	"""
	unittest.main()
