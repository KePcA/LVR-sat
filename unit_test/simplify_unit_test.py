__author__ = 'Grega'

import unittest
import SAT_implementation.bool_formulas as bf
import SAT_implementation.algorithm_utilities as au


class simplify_test(unittest.TestCase):
	"""
	Unit test for the simplify method of the algorithm utilities.
	"""

	def test_true(self):
		"""
		Tests simplifying a formula that is already simplified. Result must be Tru.
		"""
		p = bf.Tru()
		self.assertEqual(bf.Tru(), au.simplify(p), "Invalid simplification, expected Tru.")

	def test_false(self):
		"""
		Tests simplifying a formula that is already simplified. Result must be Fls.
		"""
		p = bf.Fls()
		self.assertEqual(bf.Fls(), au.simplify(p), "Invalid simplification, expected Fls.")

	def test_remove_false_from_or(self):
		"""
		Tests simplifying a formula that contains Fls in Or. Result must be Var 'a'.
		"""
		p = bf.Or([bf.Fls(), bf.Fls(), bf.Fls(), bf.Not(bf.Tru()), bf.Var("a")])
		self.assertEqual(bf.Var('a'), au.simplify(p), "Invalid simplification, expected Var 'a'.")

	def test_true_in_or(self):
		"""
		Tests simplifying a formula that contains Tru in Or. Result must be True.
		"""
		p = bf.Or([bf.Fls(), bf.Tru(), bf.Fls(), bf.Not(bf.Tru()), bf.Var("a")])
		self.assertEqual(bf.Tru(), au.simplify(p), "Invalid simplification, expected Tru.")

	def test_not_or(self):
		"""
		Tests simplifying a formula that changes an Or to a And.
		"""
		p = bf.Not(bf.Or([bf.Tru(), bf.Tru(), bf.Tru(), bf.Not(bf.Tru()), bf.Not(bf.Var("a"))]))
		self.assertEqual(bf.Fls(), au.simplify(p), "Invalid simplification, expected Fls.")

		p = bf.Not(bf.Or([bf.Fls(), bf.Fls(), bf.Fls(), bf.Not(bf.Tru()), bf.Not(bf.Var("a"))]))
		self.assertEqual(bf.Var("a"), au.simplify(p), "Invalid simplification, expected Var 'a'.")

	def test_remove_true_from_and(self):
		"""
		Tests simplifying a formula that contains Tru in And. Result must be Var 'a'.
		"""
		p = bf.And([bf.Tru(), bf.Tru(), bf.Tru(), bf.Not(bf.Fls()), bf.Var("a")])
		self.assertEqual(bf.Var('a'), au.simplify(p), "Invalid simplification, expected Var 'a'.")

	def test_false_in_and(self):
		"""
		Tests simplifying a formula that contains Fls in And. Result must be Fls'.
		"""
		p = bf.And([bf.Tru(), bf.Tru(), bf.Tru(), bf.Not(bf.Tru()), bf.Var("a")])
		self.assertEqual(bf.Fls(), au.simplify(p), "Invalid simplification, expected Tru.")

	def test_not_and(self):
		"""
		Tests simplifying a formula that changes an And to a Or.
		"""
		p = bf.Not(bf.And([bf.Tru(), bf.Tru(), bf.Tru(), bf.Not(bf.Tru()), bf.Not(bf.Var("a"))]))
		self.assertEqual(bf.Tru(), au.simplify(p), "Invalid simplification, expected Tru.")

		p = bf.Not(bf.And([bf.Tru(), bf.Tru(), bf.Tru(), bf.Not(bf.Fls()), bf.Not(bf.Var("a"))]))
		self.assertEqual(bf.Var("a"), au.simplify(p), "Invalid simplification, expected Var 'a'.")


if __name__ == '__main__':
	"""
	Runs the unit test if the script is run directly.
	"""
	unittest.main()