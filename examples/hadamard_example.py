"""
Examples of using the SAT algorithm to solve the hadamard matrix problem.
"""

__author__ = 'Grega'

import SAT_translations.hadamard_to_SAT as ha
import SAT_implementation.algorithm_DPLL as dpll
import time

def run_example(n):
	"""
	Helper method that converts the hadamard matrix of size n to a boolean formula and runs the DPLL algorithm on it.
	"""
	print "RUNNING EXAMPLE FOR n = " + str(n)

	translation_start = time.time()
	translation = ha.hadamard_translation(n)
	translation_end = time.time() - translation_start
	print "TRANSLATION OF HADAMARD MATRIX: "
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



run_example(2)
run_example(3)
run_example(4)
run_example(8)
