__author__ = 'Grega'

import unittest
import bool_formulas as bf
import SAT_implementation.algorithm_utilities as au


class remove_duplicates_unit_test(unittest.TestCase):

	def test_with_empty_list(self):
		self.assertEqual([], au.remove_duplicates([]))

	def test_with_duplicates(self):
		self.assertEqual([bf.Var("q"), bf.Var("p")], au.remove_duplicates([bf.Var("q"), bf.Var("p"), bf.Var("q"), bf.Var("p")]))

	def test_with_no_duplicates(self):
		self.assertEqual([bf.Var("q"), bf.Var("p")], au.remove_duplicates([bf.Var("q"), bf.Var("p")]))

if __name__ == '__main__':
	unittest.main()
