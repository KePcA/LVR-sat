__author__ = 'Grega'

import unittest
import SAT_implementation.bool_formulas as bf
import SAT_translations.graph_coloring_to_SAT as gc

class graph_coloring_to_SAT_unit_test(unittest.TestCase):
	"""
	Unit test for the translation of the hadamard problem to a SAT problem.
	"""

	def test_graph_coloring_1(self):
		"""
		Tests the translation of the graph coloring to a SAT problem for a given graph G and color b.
		"""
		b = 2
		G = [("a", "b"), ("a", "c"), ("b", "c"), ("d", "e"), ("e", "a")]
		g1 = bf.And([bf.Or([bf.Var("a1"), bf.Var("a2")]), bf.Or([bf.Var("c1"), bf.Var("c2")]), bf.Or([bf.Var("b1"), bf.Var("b2")]), bf.Or([bf.Var("e1"), bf.Var("e2")]), bf.Or([bf.Var("d1"), bf.Var("d2")])])
		g2 = bf.And([bf.Not(bf.And([bf.Var("a1"), bf.Var("a2")])), bf.Not(bf.And([bf.Var("c1"), bf.Var("c2")])), bf.Not(bf.And([bf.Var("b1"), bf.Var("b2")])), bf.Not(bf.And([bf.Var("e1"), bf.Var("e2")])), bf.Not(bf.And([bf.Var("d1"), bf.Var("d2")]))])
		g3 = bf.And([bf.Not(bf.And([bf.Var("a1"), bf.Var("b1")])), bf.Not(bf.And([bf.Var("a2"), bf.Var("b2")])), bf.Not(bf.And([bf.Var("a1"), bf.Var("c1")])), bf.Not(bf.And([bf.Var("a2"), bf.Var("c2")])), bf.Not(bf.And([bf.Var("b1"), bf.Var("c1")])),
					bf.Not(bf.And([bf.Var("b2"), bf.Var("c2")])), bf.Not(bf.And([bf.Var("d1"), bf.Var("e1")])), bf.Not(bf.And([bf.Var("d2"), bf.Var("e2")])), bf.Not(bf.And([bf.Var("e1"), bf.Var("a1")])), bf.Not(bf.And([bf.Var("e2"), bf.Var("a2")]))])

		result = bf.And([g1, g2, g3])
		self.assertEqual(result, gc.graph_coloring(G, b), "Invalid graph coloring for G and b = 2, expected the same as result.")

	def test_graph_coloring_2(self):
		"""
		Tests the translation of the graph coloring to a SAT problem for a given graph G and color b.
		"""
		b = 3
		G = [("a", "b"),("a", "c"),("c", "b")]
		self.assertIsNotNone(gc.graph_coloring(G, b), "Invalid graph coloring for G and b = 3, expected not None.")

if __name__ == '__main__':
	"""
	Runs the unit test if the script is run directly.
	"""
	unittest.main()