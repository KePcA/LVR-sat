#coding:utf-8

"""
Implementation of DPLL algorithm for solving SAT problem
"""

import bool_formulas as bf
import algorithm_utilities as au



#Implementation of DPLL - argument is formula in CNF form. Returns False if formula is not in SAT or
# values of variables otherwise

def DPLL(formula):

    CNF_formula = au.cnf_nnf(formula)

    """
    if not isinstance(CNF_formula, bf.And):
        raise Exception("Formula not in CNF form - CNF is not type of AND!")
    """
    values = {}

    for clause in CNF_formula.formulas:

        #First check if clause is instance of OR - it has to be otherwise formula is not in CNF
        """
        if not isinstance(clause, bf.Or):
            raise Exception("Formula is not in CNF - clause is not type of OR!")
        """
        #Check if clause is empty - has no variables. It returns false and formula is not satisfiable
        """
        if clause.isEmpty():
            raise Exception("Cannot be empty!")
        """
        #Check if it is type of unit clause - only one literal.
        if isinstance(clause, bf.Var):
            values[clause.name] = bf.Tru()

        elif isinstance(clause, bf.Not):
            values[clause.formula.name] = bf.Fls()

            """
            #Variable without negation - value is True
            if isinstance(literal, bf.Var):
                values[literal.name] = bf.Tru()
            #Variable is negated - value is False
            else:
                values[literal.formula.name] = bf.Fls()
            """

    replaced_formula = CNF_formula.replace(values)
    formula_simplified = au.simplify(replaced_formula)
    formula_cnf = au.cnf_nnf(formula_simplified)

    values_brute_force = SAT_solver_brute_force(formula_cnf, {})


    return dict(values.items() + values_brute_force.items())


#Returns all different variables which are found in formula
"""
def all_variables(CNF_formula):
    print CNF_formula
    #CNF_formula has to be type of AND
    if not isinstance(CNF_formula, bf.And):
        raise Exception("Formula not in CNF form - CNF is not type of AND!")

    variables = []

    #Iterate over each clause in CNF_formula, which has to be OR!
    for clause in CNF_formula.formulas:

        #Exception if clause is not type of OR
        if not isinstance(clause, bf.Or):
            raise Exception("Formula not in CNF form - clause is not type of OR!")

        #Iterate over variables in clause - it should only be variables or negations of variable
        for var in clause.formulas:

            #We found variable - adding into set (no repetitions)
            if isinstance(var, bf.Var):
                variables.append(var.name)

            #We found negation
            elif isinstance(var, bf.Not):

                #Inside negation is not variable - formula is not simplified nor in CNF
                if not isinstance(var.formula, bf.Var):
                    raise Exception("Formula is not simplified!")

                #Inside negation is variable - adding into set (no repetitions)
                else:
                    variables.append(var.formula.name)

            #We found OR or AND - formula is not simplified nor in CNF
            elif isinstance(var, bf.Or) or isinstance(var, bf.Not):
                raise Exception("Formula is not in CNF form inside the clause(should be only variables or not variables)!")

            #Only option left is True or False - not simplified
            else:
                raise Exception("Formula is not simplified inside the clause!")

    return au.remove_duplicates(variables)
"""


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
def DPLL_simpify(CNF_formula, dict):

    remove = False

    new_formula = bf.And([])

    for clause in CNF_formula.formulas:

        formula_OR = bf.Or([])

        #First check if clause is instance of OR - it has to be otherwise formula is not in CNF
        if not isinstance(clause, bf.Or):
            raise Exception("Formula is not in CNF!")

        for literal in clause.formulas:
            try:
                evaluation = literal.valuate(dict)
                if evaluation:
                    remove = True
                    break
                else:
                    #Removing literal of value false - if it was the last one, formula is not satisfiable - NOT WORKING!!!
                    clause.formulas.remove(literal)
                    if len(clause.formulas)==0:
                        return False
            except:
                formula_OR.formulas.append(literal)


        if remove:
            remove = False
        else:
            new_formula.formulas.append(formula_OR)

    return new_formula
"""


q = bf.Var("q")
p = bf.Var("p")
r = bf.Var("r")
test_CNF_formula = bf.And([bf.Or([q,p, r]), bf.Or([bf.Not(p), bf.Not(r)]), bf.Or([bf.Not(q)])])

test_CNF_formula.__repr__()

dictionary = {}

#replaced_formula = au.replace(dictionary, test_CNF_formula)
#print replaced_formula

#print all_variables_gen(test_CNF_formula)

#solve_dict = SAT_solver_brute_force(test_CNF_formula, dictionary)
#print solve_dict

print DPLL(test_CNF_formula)

"""
(values, formula) = DPLL(test_CNF_formula)
print values
print formula.__repr__()


variables = all_variables(test_CNF_formula)
print variables
"""
