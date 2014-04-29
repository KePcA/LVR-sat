__author__ = 'Grega'

import unittest
import SAT_implementation.bool_formulas as bf
import SAT_translations.sudoku_to_SAT as su

class sudoku_to_SAT_unit_test(unittest.TestCase):
	"""
	Unit test for the translation of the hadamard problem to a SAT problem.
	"""

	def test_sudoku_translation_1(self):
		"""
		Tests the translation of the sudoku problem to a SAT problem.
		"""
		sudoku = [[None, '8', None, '1', '6', None, None, None, '7'],
		 ['1', None, '7', '4', None, '3', '6', None, None],
		 ['3', None, None, '5', None, None, '4', '2', None],
		 [None, '9', None, None, '3', '2', '7', None, '4'],
		 [None, None, None, None, None, None, None, None, None],
		 ['2', None, '4', '8', '1', None, None, '6', None],
		 [None, '4', '1', None, None, '8', None, None, '6'],
		 [None, None, '6', '7', None, '1', '9', None, '3'],
		 ['7', None, None, None, '9', '6', None, '4', None]]
		self.assertIsNotNone(su.sudoku_translation(sudoku), "Invalid sudoku translation, expected not None.")

if __name__ == '__main__':
	"""
	Runs the unit test if the script is run directly.
	"""
	unittest.main()