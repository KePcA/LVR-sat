#coding:utf-8

"""
Translation of sudoku problem to SAT problem
"""
import bool_formulas as bf



#Method takes parameter sudoku and returns bool's formula which
def sudoku_translation(sudoku):

    formula = []

    #We visit each square in sudoku - looping over all the rows through each row to visit all the squares
    for i in range(1,10):
        for j in range(1,10):

            #Our sudoku has already a color inside it's square - we then loop through all the colors k = {1,2,...9} -
            #the variable (i,j,k) (square (i,j) is color of k) gets negated if the color is not k, otherwise not.
            if sudoku[i][j] != None:

                #Extracting color out of the square
                color = sudoku[i][j]

                #Loop through all the nine colors
                for k in range(1,10):
                    #We declare a variable of name r(i)c(j)n(k) meaning row:i , column:j , number:k
                    variable  = bf.Var("r"+str(i)+"c"+str(j)+"n"+str(k))
                    #It is color of k
                    if color==k:
                        formula.append(variable)
                    #It is not color of k
                    else:
                        formula.append(bf.Not(variable))

            #Square does not have a number
            else:

                ors = []
                for k in range(1,10):
                    variable  = bf.Var("r"+str(i)+"c"+str(j)+"n"+str(k))
                    ors.append(variable)
                    formula.append(bf.Or(ors))

        pass


