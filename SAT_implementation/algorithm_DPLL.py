#coding:utf-8

"""
Implementation of DPLL algorithm for solving SAT problem
"""

import bool_formulas as bf


#Implementation of DPLL - argument is formula in CNF form. Returns False if formula is not in SAT or
# values of variables otherwise
def DPLL(CNF_formula):

    values = {}

    for clause in CNF_formula.formulas:

        #First check if clause is instance of OR - it has to be otherwise formula is not in CNF
        if not isinstance(clause, bf.Or):
            raise Exception("Formula is not in CNF!")

        #Check if clause is empty - has no variables. It returns false and formula is not satisfiable
        if clause.isEmpty():
            return False

        #Check if it is type of unit clause - only one literal.
        if len(clause.formulas) == 1:
            literal = clause.formulas[0]
            #Variable without negation - value is True
            if isinstance(literal, bf.Var):
                values[literal.name] = True
            #Variable is negated - value is False
            else:
                values[literal.formula.name] = False



    return (values, CNF_formula)


#Returns all diferent variables which are found in formula



def DPLL_simpify(CNF_formula, dict):

    for clause in CNF_formula.formulas:

        #First check if clause is instance of OR - it has to be otherwise formula is not in CNF
        if not isinstance(clause, bf.Or):
            raise Exception("Formula is not in CNF!")

        for literal in clause.formulas:
            try:
                evaluation = literal.valuate(dict)
                if evaluation:
                    CNF_formula.formulas.remove(clause)
                    break
                else:
                    #Removing literal of value false - if it was the last one, formula is not satisfiable
                    clause.formulas.remove(literal)
                    if clause.isEmpty():
                        return False
            except:
                pass




    return CNF_formula



q = bf.Var("q")
p = bf.Var("p")
r = bf.Var("r")
test_CNF_formula = bf.And([bf.Or([q,r,p]), bf.Or([bf.Not(p)]), bf.Or([q,r,bf.Not(p)])])

(values, formula) = DPLL(test_CNF_formula)
print values
print formula.__repr__()
print DPLL_simpify(formula, values)

