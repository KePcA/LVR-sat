"""
Examples of using the SAT algorithm to solve the graph coloring problem.
"""
__author__ = 'Grega'

import time
import SAT_translations.graph_coloring_to_SAT as gc
import SAT_implementation.algorithm_DPLL as dpll

def run_example(G, b):
	"""
	Helper method that converts the graph G to a boolean formula and runs the DPLL algorithm on the specified graph G
	and number of colors b.
	Graph must be defined as a list of connections between nodes, where each connection is represented by a tuple
	(example: G = [("v1", "v2"),("v1", "v3"),("v2", "v3")])
	"""
	print "RUNNING EXAMPLE FOR NUMBER OF COLORS b = " + str(b) + " AND GRAPH G = " + str(G)

	translation_start = time.time()
	translation = gc.graph_coloring(G, b)
	translation_end = time.time() - translation_start
	print "TRANSLATION OF GRAPH: "
	print translation
	print "TIME NEEDED FOR TRANSLATION: " + str(translation_end)

	dpll_start = time.time()
	solution = dpll.DPLL(translation)
	dpll_end = time.time() - dpll_start
	if solution == False:
		print "Problem is not solvable"
	else:
		print "SOLUTION: " + str(solution)
	print "TIME NEEDED FOR DPLL: " + str(dpll_end)
	print "TOTAL TIME NEEDED: " + str(translation_end + dpll_end)
	print "-----------------------------------------------------------------------------------------------------------------\n"

run_example([("a", "b"), ("a", "c"), ("b", "c"), ("d", "e"), ("e", "a")], 2)
run_example([("a", "b"),("a", "c"),("c", "b")], 3)