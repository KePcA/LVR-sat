#coding:utf-8

"""
Implementation of DPLL algorithm for solving SAT problem
"""

import SAT_implementation.bool_formulas as bf
import SAT_implementation.algorithm_utilities as au

def DPLL(formula):
	"""
	Implementation of DPLL - argument is formula in CNF form. Returns False if formula is not in SAT or values of variables otherwise.
	"""
	CNF_formula = au.simplify(au.cnf_nnf(formula))

	values = {}
	while True:
		if isinstance(CNF_formula, bf.Tru) or isinstance(CNF_formula, bf.Fls) or isinstance(CNF_formula, bf.Var) or isinstance(CNF_formula, bf.Not):
		# Formula is only True, False, Var or negated Var - no more pure vars / literals, we finished
			break

		temp_value = {}
		for clause in CNF_formula.formulas:
			if isinstance(clause, bf.Var):
				#It is only literal - Var
				values[clause.name] = bf.Tru()
				temp_value[clause.name] = bf.Tru()
				break
			elif isinstance(clause, bf.Not):
				# It is only literal - negated Var
				values[clause.formula.name] = bf.Fls()
				temp_value[clause.formula.name] = bf.Fls()
				break

		if temp_value:
			#We found literal - replace formula with its value, simplify, put in cnf and look for literal again
			replaced_formula = CNF_formula.replace(temp_value)
			formula_simplified = au.simplify(replaced_formula)
			CNF_formula = au.cnf_nnf(formula_simplified)
		else:
			#finish, no more literals
			break

	#Check for pure variables
	pure_var_values = au.pure_variables(CNF_formula)
	replaced_formula = CNF_formula.replace(pure_var_values)
	formula_simplified = au.simplify(replaced_formula)
	CNF_formula = au.cnf_nnf(formula_simplified)

	#Solve the rest of formula by brute force
	values_brute_force = SAT_solver_brute_force(CNF_formula, {})
	if values_brute_force is not None:
		# satisfiable problem
		return dict(values.items() + pure_var_values.items() + values_brute_force.items())
	else:
		# unsatisfiable problem
		return False



#Solves SAT problem by trying all the possibilities for variables in formula - WORKING
def SAT_solver_brute_force(CNF_formula, dictionary):
	if isinstance(CNF_formula, bf.Tru):
		#Formula is Tru / satisfiable - return dictionary with given values of variables
		return dictionary
	elif isinstance(CNF_formula, bf.Fls):
		# Formula is Fls -/ not satisfiable -  return None
		return None

	else:
		# Take first variable and set its value to True
		variables = au.extract_variables(CNF_formula)
		dictionary[variables[0]] = bf.Tru()
		simplified_formula = CNF_formula.replace(dictionary)
		simplified_formula = au.simplify(simplified_formula)
		result = SAT_solver_brute_force(simplified_formula, dictionary)

		if result is not None:
			# Return dictionary if formula is satisfiable
			return result
		else:
			# Set same variable to False and try to solve again again
			dictionary[variables[0]] = bf.Fls()
			# replace and simplify formula
			simplified_formula = au.simplify(CNF_formula.replace(dictionary) )
			return SAT_solver_brute_force(simplified_formula, dictionary)
