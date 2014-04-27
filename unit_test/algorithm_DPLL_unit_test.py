__author__ = 'Grega'


import unittest
import SAT_implementation.bool_formulas as bf
import SAT_implementation.algorithm_DPLL as dpll

class algorithm_DPLL_unit_test(unittest.TestCase):
	"""
	Unit test for the DPLL algorithm.
	"""

	def test_satisfiable_formula_1(self):
		"""
		Tests the DPLL algorithm with the specified satisfiable formula.
		"""
		a = bf.Var("a")
		b = bf.Var("b")
		c = bf.Var("c")
		formula = bf.And([bf.Or([b, a, c]), bf.Or([bf.Not(a), bf.Not(c)]), bf.Or([bf.Not(b)])])
		result = {'a': bf.Tru(), 'b': bf.Fls(), 'c': bf.Fls()}
		self.assertEqual(result, dpll.DPLL(formula), "Invalid values for formula 1, expected the same as result.")

	def test_satisfiable_formula_2(self):
		"""
		Tests the DPLL algorithm with the specified satisfiable formula.
		"""
		a = bf.Var("a")
		b = bf.Var("b")
		c = bf.Var("c")
		formula = bf.And([bf.Not(a), bf.Or([a, bf.Not(b)]), bf.Or([a, b, c])])
		result = {'a': bf.Fls(), 'b': bf.Fls(), 'c': bf.Tru()}
		self.assertEqual(result, dpll.DPLL(formula), "Invalid values for formula 2, expected the same as result.")

	def test_satisfiable_formula_3(self):
		"""
		Tests the DPLL algorithm with the specified satisfiable formula.
		"""
		a = bf.Var("a")
		b = bf.Var("b")
		c = bf.Var("c")
		formula = bf.And([bf.Or([a, b, c]), bf.Or([a, bf.Not(b), c])])
		result = {'a': bf.Tru(), 'c': bf.Tru()}
		self.assertEqual(result, dpll.DPLL(formula), "Invalid values for formula 3, expected the same as result.")

	def test_satisfiable_formula_4(self):
		"""
		Tests the DPLL algorithm with the specified satisfiable formula.
		"""
		a = bf.Var("a")
		b = bf.Var("b")
		c = bf.Var("c")
		formula = bf.And([a, bf.Or([bf.Not(a), b]), bf.Or([bf.Not(a), bf.Not(b), bf.Not(c)])])
		result = {'a': bf.Tru(), 'b': bf.Tru(), 'c': bf.Fls()}
		self.assertEqual(result, dpll.DPLL(formula), "Invalid values for formula 4, expected the same as result.")

	def test_satisfiable_formula_5(self):
		"""
		Tests the DPLL algorithm with the specified satisfiable formula.
		"""
		a = bf.Var("a")
		b = bf.Var("b")
		c = bf.Var("c")
		formula = bf.And([a, bf.And([b, a]), bf.Or([c, b])])
		result = {'a': bf.Tru(), 'b': bf.Tru()}
		self.assertEqual(result, dpll.DPLL(formula), "Invalid values for formula 5, expected the same as result.")

	def test_satisfiable_formula_6(self):
		"""
		Tests the DPLL algorithm with the specified satisfiable formula.
		"""
		a = bf.Var("a")
		b = bf.Var("b")
		c = bf.Var("c")
		formula = bf.And([bf.Not(a), bf.Or([bf.And([a, b, c]), bf.Not(b)])])
		result = {'a': bf.Fls(), 'b': bf.Fls()}
		self.assertEqual(result, dpll.DPLL(formula), "Invalid values for formula 6, expected the same as result.")

	def test_satisfiable_formula_7(self):
		"""
		Tests the DPLL algorithm with the specified satisfiable formula.
		"""
		a = bf.Var("a")
		b = bf.Var("b")
		c = bf.Var("c")
		formula = bf.Or([bf.Not(a), bf.And([bf.Or([a, b, c]), bf.Not(b)])])
		result = {'a': bf.Tru(), 'b': bf.Fls(), 'c': bf.Tru()}
		self.assertEqual(result, dpll.DPLL(formula), "Invalid values for formula 7, expected the same as result.")

	def test_satisfiable_formula_8(self):
		"""
		Tests the DPLL algorithm with the specified satisfiable formula.
		"""
		formula = bf.Tru()
		result = {}
		self.assertEqual(result, dpll.DPLL(formula), "Invalid values for formula 8, expected the same as result.")

	def test_unsatisfiable_formula_1(self):
		"""
		Tests the DPLL algorithm with the specified unsatisfiable formula.
		"""
		a = bf.Var("a")
		b = bf.Var("b")
		c = bf.Var("c")
		d = bf.Var("d")
		formula = bf.And([bf.Not(a), bf.Or([bf.And([b, c, d]), bf.Not(c)]), a])
		self.assertFalse(dpll.DPLL(formula), "Invalid values for formula 1, expected False.")

	def test_unsatisfiable_formula_2(self):
		"""
		Tests the DPLL algorithm with the specified unsatisfiable formula.
		"""
		formula = bf.Fls()
		self.assertFalse(dpll.DPLL(formula), "Invalid values for formula 2, expected False.")

if __name__ == '__main__':
	"""
	Runs the unit test if the script is run directly.
	"""
	unittest.main()