import unittest
import bool_formulas as bf
import SAT_implementation.algorithm_utilities as au

class simplify_test(unittest.TestCase):

	def test_true(self):
		self.assertTrue(au.simplify(bf.Tru()).evaluate())

	def test_remove_false_from_or(self):
		p = bf.Or([bf.Fls(), bf.Fls(), bf.Fls(), bf.Not(bf.Tru()), bf.Var("x")])
		simplify = au.simplify(p)
		self.assertEqual(bf.Var('x'), simplify)

	def test_remove_true_from_and(self):
		p = bf.And([bf.Tru(), bf.Tru(), bf.Tru(), bf.Not(bf.Fls()), bf.Var("x")])
		simplify = au.simplify(p)
		self.assertEqual(bf.Var('x'), simplify)


if __name__ == '__main__':
    unittest.main()