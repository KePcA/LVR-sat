__author__ = 'Grega'

"""
Translation of sudoku problem to SAT problem
"""
import SAT_implementation.bool_formulas as bf

def sudoku_translation(sudoku):
	"""
	Converts the specified sudoku and returns the representation of the sudoku as a boolean formula.
	"""
	formula = []

	#We visit each square in sudoku - looping over all the rows through each row to visit all the squares
	for i in range(9):
		for j in range(9):

			#Our sudoku has already a color inside it's square - we then loop through all the colors k = {1,2,...9} -
			#the variable (i,j,k) (square (i,j) is color of k) gets negated if the color is not k, otherwise not.
			if sudoku[i][j] != None:

				#Extracting color out of the square
				color = sudoku[i][j]

				#Loop through all the nine colors
				for k in range(9):
					#We declare a variable of name r(i)c(j)n(k) meaning row:i , column:j , number:k
					variable = bf.Var("r" + str(i)+"c" + str(j) + "n" + str(k))
					#It is color of k
					if color == k+1:
						formula.append(variable)

			#Square does not have a number
			else:
				#Each square can only have one number
				for k in range(9):
					ORs = bf.Or([])
					ORs.formulas.append(bf.Not(bf.Var("r%dc%do%d" % (i, j, k))))
					ANDs = bf.And([])
					for l in range(9):
						if l == k:
							ANDs.formulas.append(bf.Var("r%dc%dv%d" % (i, j, l)))
						else:
							ANDs.formulas.append(bf.Not(bf.Var("r%dc%dv%d" % (i, j, l))))
					ORs.formulas.append(ANDs)
					formula.append(ORs)

				ORs_1 = bf.Or([])
				for k in range(9):
					ORs_1.formulas.append(bf.Var("r%dc%do%d" % (i, j, k)))
				formula.append(ORs_1)


			#Each row contains exactly one of each number from 1 to 9
			ORs_2 = bf.Or([])
			for k in range(9):
				ORs_2.formulas.append(bf.Var("r%dc%dv%d" % (j, k, i)) )
			formula.append(ORs_2)

			#Each column contains exactly one of each number from 1 to 9
			ORs_3 = bf.Or([])
			for k in range(9):
				ORs_3.formulas.append(bf.Var("r%dc%dv%d" % (k, j, i)) )
			formula.append(ORs_3)

		#Each of 3x3 square contains exactly one of each number from 1 to 9
		for j in range(3):
			for k in range(3):
				ORs_4 = bf.Or([])
				for y in range(3):
					for x in range(3):
						ORs_4.formulas.append(bf.Var("r%dc%dv%d" % (3*j+x, 3*k+y, i)))
				formula.append(ORs_4)

	return bf.And(formula)
