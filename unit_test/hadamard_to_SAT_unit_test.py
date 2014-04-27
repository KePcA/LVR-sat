__author__ = 'Grega'

import unittest
import SAT_implementation.bool_formulas as bf
import SAT_translations.hadamard_to_SAT as ha

class hadamard_to_SAT_unit_test(unittest.TestCase):
	"""
	Unit test for the translation of the hadamard problem to a SAT problem.
	"""

	def test_hadamard_translation_1(self):
		"""
		Tests the translation of the hadamard problem of size 1 to a SAT problem.
		"""
		n = 1
		translation = ha.hadamard_translation(n)
		result = bf.Fls()
		self.assertEqual(result, translation, "Invalid hadamard translation for n = 1, expected the same as result.")

	def test_hadamard_translation_2(self):
		"""
		Tests the translation of the hadamard problem of size 2 to a SAT problem.
		"""
		n = 2
		translation = ha.hadamard_translation(n)
		print translation
		self.assertNotEqual(bf.Fls(), translation, "Invalid hadamard translation for n = 2, expected not Fls.")

	def test_hadamard_translation_3(self):
		"""
		Tests the translation of the hadamard problem of size 3 to a SAT problem.
		"""
		n = 3
		translation = ha.hadamard_translation(n)
		result = bf.Fls()
		self.assertEqual(result, translation, "Invalid hadamard translation for n = 3, expected not Fls.")

	def test_hadamard_translation_4(self):
		"""
		Tests the translation of the hadamard problem of size 4 to a SAT problem.
		"""
		n = 4
		translation = ha.hadamard_translation(n)
		self.assertNotEqual(bf.Fls(), translation, "Invalid hadamard translation for n = 4, expected not Fls.")

	def test_hadamard_translation_8(self):
		"""
		Tests the translation of the hadamard problem of size 8 to a SAT problem.
		"""
		n = 8
		translation = ha.hadamard_translation(n)
		self.assertNotEqual(bf.Fls(), translation, "Invalid hadamard translation for n = 8, expected not Fls.")

if __name__ == '__main__':
	"""
	Runs the unit test if the script is run directly.
	"""
	unittest.main()