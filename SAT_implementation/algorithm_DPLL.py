#coding:utf-8

"""
Implementation of DPLL algorithm for solving SAT problem
"""
from SAT_implementation import algorithm_utilities as au
from SAT_implementation import bool_formulas as bf


#Implementation of DPLL - argument is formula in CNF form. Returns False if formula is not in SAT or
# values of variables otherwise

def DPLL(formula):

    CNF_formula = au.cnf_nnf(formula)
    values = {}
    while True:
        print CNF_formula
        #Formula is only True, False, Var or negated Var - no more pure vars / literals, we finished
        if isinstance(CNF_formula, bf.Tru) or isinstance(CNF_formula, bf.Fls) or isinstance(CNF_formula, bf.Var) or isinstance(CNF_formula, bf.Not): break

        temp_value = {}
        for clause in CNF_formula.formulas:

            #It is only literal - Var
            if isinstance(clause, bf.Var):
                values[clause.name] = bf.Tru()
                temp_value[clause.name] = bf.Tru()
                break

            #It is only literal - negated Var
            elif isinstance(clause, bf.Not):
                values[clause.formula.name] = bf.Fls()
                temp_value[clause.formula.name] = bf.Fls()
                break

        #We found literal - replace formula with its value, simplify, put in cnf and look for literal again
        if temp_value:
            replaced_formula = CNF_formula.replace(temp_value)
            formula_simplified = au.simplify(replaced_formula)
            CNF_formula = au.cnf_nnf(formula_simplified)
        #finish, no more literals
        else:
            break

    #Check for pure variables
    pure_var_values = au.pure_variables(CNF_formula)
    replaced_formula = CNF_formula.replace(pure_var_values)
    formula_simplified = au.simplify(replaced_formula)
    CNF_formula = au.cnf_nnf(formula_simplified)

    #Solve the rest of formula by brute force
    values_brute_force = SAT_solver_brute_force(CNF_formula, {})

    return dict(values.items() + pure_var_values.items() + values_brute_force.items())



#Solves SAT problem by trying all the possibilities for variables in formula - WORKING
def SAT_solver_brute_force(CNF_formula, dictionary):
    #Formula is Tru / satisfiable - return dictionary with given values of variables
    if isinstance(CNF_formula, bf.Tru):
        return dictionary

    #Foruma is Fls -/ not satisfiable -  return False
    elif isinstance(CNF_formula, bf.Fls):
        return None

    else:
        #Take first variable and set its value to True
        variables = au.extract_variables(CNF_formula)
        dictionary[variables[0]] = bf.Tru()
        simplified_formula = CNF_formula.replace(dictionary)
        simplified_formula = au.simplify(simplified_formula)
        result = SAT_solver_brute_force(simplified_formula, dictionary)

        #Return dictionary if formula is SAT
        if result is not None:
            return result

        #Set same variable to False and try to solve again again
        else:
            dictionary[variables[0]] = bf.Fls()
            simplified_formula = CNF_formula.replace(dictionary) #simplify(CNF_formula, dictionary)
            simplified_formula = au.simplify(simplified_formula)
            return SAT_solver_brute_force(simplified_formula, dictionary)



"""
TESTING
"""
q = bf.Var("q")
p = bf.Var("p")
r = bf.Var("r")
test_CNF_formula_1 = bf.And([bf.Or([q,p, r]), bf.Or([bf.Not(p), bf.Not(r)]), bf.Or([bf.Not(q)])])
test_CNF_formula_2 = bf.And([bf.Not(p), bf.Or([p,bf.Not(q)]), bf.Or([p,q,r])])
test_CNF_formula_3 = bf.And([bf.Or([p,q,r]), bf.Or([p,bf.Not(q),r])])
test_CNF_formula_4 = bf.And([p, bf.Or([bf.Not(p), q]), bf.Or([bf.Not(p), bf.Not(q), bf.Not(r)])])

dictionary = {}

"""
print '\n'
print(test_CNF_formula_1)
print DPLL(test_CNF_formula_1)
print '\n'
print(test_CNF_formula_2)
print DPLL(test_CNF_formula_2)
print '\n'
print(test_CNF_formula_3)
print DPLL(test_CNF_formula_3)
"""
print DPLL(test_CNF_formula_4)

