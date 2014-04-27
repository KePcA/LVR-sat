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
					variable  = bf.Var("r"+str(i+1)+"c"+str(j+1)+"n"+str(k+1))
					#It is color of k
					if color==k+1:
						formula.append(variable)
					#It is not color of k
					else:
						formula.append(bf.Not(variable))

			#Square does not have a number
			else:

				#Each square can only have one number
				ORs_1 = bf.Or([])
				for k in range(9):
					ANDs = bf.And([])
					for l in range(9):
						variable = bf.Var("r"+str(i+1)+"c"+str(j+1)+"n"+str(k+1))
						if k==l:
							ANDs.formulas.append(variable)
						else:
							ANDs.formulas.append(bf.Not(variable))
					ORs_1.formulas.append(ANDs)
				formula.append(ORs_1)

				#Each row contains exactly one of each number from 1 to 9
				ORs_2 = bf.Or([])
				for k in range(9):
					variable = bf.Var("r"+str(j+1)+"c"+str(k+1)+"n"+str(i+1))
					ORs_2.formulas.append(variable)
				formula.append(ORs_2)

				#Each column contains exactly one of each number from 1 to 9
				ORs_3 = bf.Or([])
				for k in range(9):
					variable = bf.Var("r"+str(k+1)+"c"+str(j+1)+"n"+str(i+1))
					ORs_3.formulas.append(variable)
				formula.append(ORs_3)

		#Each of 3x3 square contains exactly one of each number from 1 to 9
		for j in range(3):
			for k in range(3):
				ORs_4 = bf.Or([])
				for m in range(3):
					for n in range(3):
						variable = bf.Var("r"+str(3*j+n+1)+"c"+str(3*k+m+1)+"n"+str(i+1))
						ORs_4.formulas.append(variable)
				formula.append(ORs_4)

	return bf.And(formula)
