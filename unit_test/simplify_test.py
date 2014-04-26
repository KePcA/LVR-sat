from SAT_implementation import bool_formulas as bf

import unittest
import SAT_implementation.algorithm_utilities as au


class simplify_test(unittest.TestCase):

	def test_true(self):
		p = bf.Tru()
		self.assertEqual(bf.Tru(), au.simplify(p))

	def test_false(self):
		p = bf.Fls()
		self.assertEqual(bf.Fls(), au.simplify(p))

	def test_remove_false_from_or(self):
		p = bf.Or([bf.Fls(), bf.Fls(), bf.Fls(), bf.Not(bf.Tru()), bf.Var("x")])
		self.assertEqual(bf.Var('x'), au.simplify(p))

	def test_true_in_or(self):
		p = bf.Or([bf.Fls(), bf.Tru(), bf.Fls(), bf.Not(bf.Tru()), bf.Var("x")])
		self.assertEqual(bf.Tru(), au.simplify(p))

	def test_not_or(self):
		p = bf.Not(bf.Or([bf.Tru(), bf.Tru(), bf.Tru(), bf.Not(bf.Tru()), bf.Not(bf.Var("x"))]))
		self.assertEqual(bf.Fls(), au.simplify(p))

		p = bf.Not(bf.Or([bf.Fls(), bf.Fls(), bf.Fls(), bf.Not(bf.Tru()), bf.Not(bf.Var("x"))]))
		self.assertEqual(bf.Var("x"), au.simplify(p))

	def test_remove_true_from_and(self):
		p = bf.And([bf.Tru(), bf.Tru(), bf.Tru(), bf.Not(bf.Fls()), bf.Var("x")])
		self.assertEqual(bf.Var('x'), au.simplify(p))

	def test_false_in_and(self):
		p = bf.And([bf.Tru(), bf.Tru(), bf.Tru(), bf.Not(bf.Tru()), bf.Var("x")])
		self.assertEqual(bf.Fls(), au.simplify(p))

	def test_not_and(self):
		p = bf.Not(bf.And([bf.Tru(), bf.Tru(), bf.Tru(), bf.Not(bf.Tru()), bf.Not(bf.Var("x"))]))
		self.assertEqual(bf.Tru(), au.simplify(p))

		p = bf.Not(bf.And([bf.Tru(), bf.Tru(), bf.Tru(), bf.Not(bf.Fls()), bf.Not(bf.Var("x"))]))
		self.assertEqual(bf.Var("x"), au.simplify(p))


if __name__ == '__main__':
	unittest.main()