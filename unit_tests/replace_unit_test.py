__author__ = 'Grega'

import unittest
import SAT_implementation.bool_formulas as bf

class replace_unit_test(unittest.TestCase):
	"""
	Unit test for the replace values method of the algorithm utilities.
	"""

	def test_replacing_one_value(self):
		"""
		Tests replacing only on value.
		"""
		a = bf.Var("a")
		b = bf.Var("b")
		c = bf.Var("c")
		values = {"a": bf.Tru()}
		formula = bf.And([bf.Or([b, a, c]), bf.Or([bf.Not(a), bf.Not(c)]), bf.Or([bf.Not(b)])])
		result = bf.And([bf.Or([b, bf.Tru(), c]), bf.Or([bf.Not(bf.Tru()), bf.Not(c)]), bf.Or([bf.Not(b)])])
		self.assertEqual(result, formula.replace(values), "Invalid replacement, expected the same as specified by result.")

	def test_replacing_all_values(self):
		a = bf.Var("a")
		b = bf.Var("b")
		c = bf.Var("c")
		values = {"b": bf.Tru(), "a": bf.Fls(), "c": bf.Tru()}
		formula = bf.Not(bf.Or([bf.And([bf.Not(b), a, c]), bf.Not(bf.Or([b, bf.Not(a), bf.Tru()]))]))
		result = bf.Not(bf.Or([bf.And([bf.Not(bf.Tru()), bf.Fls(), bf.Tru()]), bf.Not(bf.Or([bf.Tru(), bf.Not(bf.Fls()), bf.Tru()]))]))
		self.assertEqual(result, formula.replace(values), "Invalid replacement, expected the same as specified by result.")

if __name__ == '__main__':
	"""
	Runs the unit test if the script is run directly.
	"""
	unittest.main()
