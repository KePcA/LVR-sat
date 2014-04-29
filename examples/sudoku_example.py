"""
Examples of using the SAT algorithm to solve a sudoku.
"""
__author__ = 'Grega'

import time
import SAT_translations.sudoku_to_SAT as su
import SAT_implementation.algorithm_DPLL as dpll

def printSudoku(sudoku):
	"""
	Prints the specified sudoku tu a human readable form
	"""
	printout = ""

	for i in range(9):
		if i % 3 == 0:
			printout += "  "
			for _ in xrange(17):
				printout += "--"
			printout += "-\n"

		for j in range(9):
			if j % 3 == 0:
				printout += " | "

			if sudoku[i][j] is not None:
				printout += " " + str(sudoku[i][j]) + " "
			else:
				printout += " - "

		printout += " |"

		printout += "\n"

	printout += "  "
	for _ in xrange(17):
		printout += "--"
	printout += "-\n"

	print printout


def run_example(sudoku):
	"""
	Helper method that converts the specified sudoku to a boolean formula and runs the DPLL algorithm on it.
	The sudoku must be defined as an array with nine rows, where each for is represented by nine elements (elements can
	be None for no value or 1 .. 9).
	"""
	print "RUNNING EXAMPLE FOR SUDOKU: "
	printSudoku(sudoku)

	translation_start = time.time()
	translation = su.sudoku_translation(sudoku)
	translation_end = time.time() - translation_start
	print "TRANSLATION OF SUDOKU: "
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

sudoku1 = [[None, 8, None, 1, 6, None, None, None, 7],
		[1, None, 7, 4, None, 3, 6, None, None],
		[3, None, None, 5, None, None, 4, 2, None],
		[None, 9, None, None, 3, 2, 7, None, 4],
		[None, None, None, None, None, None, None, None, None],
		[2, None, 4, 8, 1, None, None, 6, None],
		[None, 4, 1, None, None, 8, None, None, 6],
		[None, None, 6, 7, None, 1, 9, None, 3],
		[7, None, None, None, 9, 6, None, 4, None]]

sudoku2 = [[None, 3, 5, 2, 6, 9, 7, 8, 1],
		[6, 8, 2, 5, 7, 1, 4, 9, 3],
		[1, 9, 7, 8, 3, 4, 5, 6, 2],
		[8, 2, 6, 1, 9, 5, 3, 4, 7],
		[3, 4, 7, 6, 8, 2, 9, 1, 5],
		[9, 5, 1, 7, 4, 3, 6, 2, 8],
		[5, 1, 9, 3, 2, 6, 8, 7, 4],
		[2, 4, 8, 9, 5, 7, 1, 3, 6],
		[7, 6, 3, 4, 1, 8, 2, 5, 9]]


run_example(sudoku2)