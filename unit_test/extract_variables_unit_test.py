__author__ = 'Grega'

import unittest
import bool_formulas as bf
import SAT_implementation.algorithm_utilities as au


class extract_values_unit_test(unittest.TestCase):

	def test_simple_extraction_of_values(self):
		q = bf.Var("q")
		p = bf.Var("p")
		self.assertEqual(["p", "q"], au.extract_variables(bf.And([q, p])))

	def test_complex_extraction_of_values(self):
		q = bf.Var("q")
		p = bf.Var("p")
		r = bf.Var("r")
		formula = bf.And([bf.Or([q, p, r]), bf.Or([bf.Not(p), bf.Not(r)]), bf.Not(q)])
		self.assertEqual(["p", "q", "r"], au.extract_variables(formula))

	def test_extracting_one_value(self):
		self.assertEqual(["q"], au.extract_variables(bf.Var("q")))

	def test_extracting_no_values(self):
		formula = bf.And([bf.Or([bf.Tru(), bf.Tru(), bf.Tru()]), bf.Or([bf.Not(bf.Tru()), bf.Not(bf.Tru())]), bf.Not(bf.Tru())])
		self.assertEqual([], au.extract_variables(formula))

if __name__ == '__main__':
	unittest.main()
