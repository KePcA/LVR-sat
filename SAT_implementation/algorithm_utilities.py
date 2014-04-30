"""
Utility methods used in DPLL algorithm.
"""

__author__ = 'Grega'

import SAT_implementation.bool_formulas as bf
import itertools

def cnf_nnf(p):
	"""
	Converts the specified p formula to a NNF form and then to a CNF form.
	"""
	nnf_p = nnf(p)
	return cnf(nnf_p)


def cnf(p):
	"""
	Converts the specified p formula to a CNF form.
	"""
	if isinstance(p, bf.And):
		return flatten(bf.And(map(lambda x: cnf(x), p.formulas)))
	elif isinstance(p, bf.Or):
		f_length = len(p.formulas)
		if f_length == 0:
			return bf.Fls()
		elif f_length == 1:
			return cnf(p.formulas[0])
		else:
			flattened = flatten(p)
			if isinstance(flattened, bf.Or) or isinstance(flattened, bf.And):
				flattened_cnf = map(lambda x: cnf(x), flattened.formulas)
				disjunctions = filter(lambda x: not isinstance(x, bf.And), flattened_cnf)
				if len(flattened_cnf) == len(disjunctions):
					return bf.Or(disjunctions)
				else:
					conjunctions = filter(lambda x: isinstance(x, bf.And), flattened_cnf)
					return flatten(bf.And(map(lambda x: cnf(bf.Or([x] + disjunctions + conjunctions[1:])), conjunctions[0].formulas)))
			else:
				return flattened
	else:
		return p


def flatten(p):
	"""
	Flattens the specified p formula.
	"""
	if isinstance(p, bf.Tru) or isinstance(p, bf.Fls) or isinstance(p, bf.Var):
		# Nothing to be done, return p
		return p
	if isinstance(p, bf.Not):
		x = p.formula
		if isinstance(x, bf.Not):
			# Get rid of Not, return the flattened formula.
			return flatten(x.formula)
		elif isinstance(x, bf.Or):
			# Convert to And(Not(y1), ...,Not(yn)) and flatten the formula.
			return flatten(bf.And(map(lambda y: bf.Not(y), x.formulas)))
		elif isinstance(x, bf.And):
			# Convert to Or(Not(y1), ...,Not(yn)) and flatten the formula.
			return flatten(bf.Or(map(lambda y: bf.Not(y), x.formulas)))
		else:
			return p
	elif isinstance(p, bf.Or):
		flattened = map(lambda x: flatten(x), p.formulas)
		length = len(flattened)
		if length == 0:
			return bf.Fls()
		elif length == 1:
			return flattened[0]
		else:
			formulas = sum([x.formulas if isinstance(x, bf.Or) else [x] for x in flattened], [])
			if __any__(formulas, lambda x: isinstance(x, bf.Tru)):
				return bf.Tru()
			else:
				return bf.Or(formulas)
	elif isinstance(p, bf.And):
		flattened = map(lambda x: flatten(x), p.formulas)
		length = len(flattened)
		if length == 0:
			return bf.Tru()
		elif length == 1:
			return flattened[0]
		else:
			formulas = sum([x.formulas if isinstance(x, bf.And) else [x] for x in flattened], [])
			if __any__(formulas, lambda x: isinstance(x, bf.Fls)):
				return bf.Fls()
			else:
				return bf.And(formulas)


def nnf(p):
	"""
	Converts the specified p formula to a NNF form.
	"""
	if isinstance(p, bf.Tru) or isinstance(p, bf.Fls) or isinstance(p, bf.Var):
		return p
	elif isinstance(p, bf.Not):
		x = p.formula
		if isinstance(x, bf.Tru):
			return bf.Fls()
		elif isinstance(x, bf.Fls):
			return bf.Tru()
		elif isinstance(x, bf.Var):
			return p
		elif isinstance(x, bf.Not):
			return nnf(x.formula)
		elif isinstance(x, bf.Or):
			return bf.And(map(lambda y: nnf(bf.Not(y)), x.formulas))
		elif isinstance(x, bf.And):
			return bf.Or(map(lambda y: nnf(bf.Not(y)), x.formulas))
	elif isinstance(p, bf.Or):
			return bf.Or(map(nnf, p.formulas))
	elif isinstance(p, bf.And):
			return bf.And(map(nnf, p.formulas))

def simplify(p, use_absorptions = False):
	"""
	Simplified the specified p formula. Use absorptions is by default set to False because it causes a slow down in
	performance.
	"""
	if isinstance(p, bf.Tru) or isinstance(p, bf.Fls) or isinstance(p, bf.Var):
		# Values that can't be simplified any further.
		return p
	elif isinstance(p, bf.Not):
		# Not simplification.
		x = p.formula
		if isinstance(x, bf.Tru):
			# Not(Tru) -> Fls
			return bf.Fls()
		elif isinstance(x, bf.Fls):
			# Not(Fls) -> Tru
			return bf.Tru()
		elif isinstance(x, bf.Var):
			# Not(Var(x)) -> Not(Var(x))
			return p
		elif isinstance(x, bf.Not):
			# Not(Not(x)) -> x
			return simplify(x.formula, use_absorptions)
		elif isinstance(x, bf.Or):
			# Or(y1,...,yn) -> And(Not(y1),...Not(yn))
			return simplify(bf.And(map(lambda y: bf.Not(y), x.formulas)), use_absorptions)
		elif isinstance(x, bf.And):
			# And(y1,...,yn) -> Or(Not(y1),...Not(yn))
			return simplify(bf.Or(map(lambda y: bf.Not(y), x.formulas)), use_absorptions)
	elif isinstance(p, bf.Or):
		# Simplify sub-formulas
		simplified = map(lambda y: simplify(y, use_absorptions), p.formulas)
		# Merge and remove duplicates.
		formulas = remove_duplicates(sum([x.formulas if isinstance(x, bf.Or) else [x] for x in simplified], []))
		length = len(formulas)
		if length == 0:
			return bf.Fls()
		if length == 1:
			return formulas[0]
		else:
			if use_absorptions:
				# Find all of the or absorptions
				absorption, absorption_tuples = __find_absorptions__(formulas, bf.And)
				# Remove all of the absorptions
				formulas = filter(lambda x: x not in absorption, formulas)
				# Extend the list wit new absorptions
				formulas.extend([simplify(bf.Or([z for z in x.formulas if z not in y]), use_absorptions) for x, y in absorption_tuples])
				# Remove duplicates
				formulas = remove_duplicates(formulas)
			# Remove all falses. Because of order (F, T, Var, Not, And, Or) only first element needs to be checked for removal.
			if length > 0 and isinstance(formulas[0], bf.Fls):
				formulas = formulas[1:]
			# If one is true, true must be returned. Because of order (F, T, Var, Not, And, Or) and filtering only first element needs to be checked.
			length = len(formulas)
			if length > 0 and isinstance(formulas[0], bf.Tru):
				return bf.Tru()
			# If there is an element x that is equal to Not and the value of Not is also contained in the formulas return true
			if __any__(formulas, lambda x: isinstance(x, bf.Not) and x.formula in formulas):
					return bf.Tru()
			# Recheck current length of formulas
			if length == 0:
				return bf.Tru()
			if length == 1:
				return formulas[0]
			else:
				return bf.Or(formulas)
	elif isinstance(p, bf.And):
		# Simplify sub-formulas
		simplified = map(lambda y: simplify(y, use_absorptions), p.formulas)
		# Merge and remove duplicates.
		formulas = remove_duplicates(sum([x.formulas if isinstance(x, bf.And) else [x] for x in simplified], []))
		length = len(formulas)
		if length == 0:
			return bf.Tru()
		if length == 1:
			return formulas[0]
		else:
			if use_absorptions:
				# Find all of the and absorptions
				absorption, absorption_tuples = __find_absorptions__(formulas, bf.Or)
				# Remove all of the absorptions
				formulas = filter(lambda x: x not in absorption, formulas)
				# Extend the list wit new absorptions
				formulas.extend([simplify(bf.Or([z for z in x.formulas if z not in y]), use_absorptions) for x, y in absorption_tuples])
				# Remove duplicates
				formulas = remove_duplicates(formulas)
			# Remove all trues. Because of order (F, T, Var, Not, And, Or) only first and second element needs to be checked for removal.
			if length > 0 and isinstance(formulas[0], bf.Tru):
				formulas = formulas[1:]
			elif length > 1 and isinstance(formulas[1], bf.Tru):
				del formulas[1]
			# If one is false, false must be returned. Because of order (F, T, Var, Not, And, Or) only first element needs to be checked.
			length = len(formulas)
			if length > 0 and isinstance(formulas[0], bf.Fls):
				return bf.Fls()
			# If there is an element x that is equal to Not and the value of Not is also contained in the formulas return false
			if __any__(formulas, lambda x: isinstance(x, bf.Not) and x.formula in formulas):
				return bf.Fls()
			# Recheck current length of formulas
			if length == 0:
				return bf.Tru()
			if length == 1:
				return formulas[0]
			else:
				return bf.And(formulas)


def __find_absorptions__(lst, class_value):
	"""
	Finds all of the absorptions fo the specified class_value and adds them to a list. Besides the list a list of tuples
	(x, absorb) is returned.
	"""
	absorptions = []
	absorption_tuples = []
	for x in lst:
		if isinstance(x, class_value):
			tmp = []
			for y in lst:
				if isinstance(y, bf.Not) and y.formula in x.formulas:
					tmp.append(y)
				elif bf.Not(y) in x.formulas:
					tmp.append(bf.Not(y))
			if len(tmp) != 0:
				absorptions.append(x)
				absorption_tuples.append((x, tmp))
	return absorptions, absorption_tuples


def __any__(formulas, funct):
	"""
	Implementation of a method that receives a list of values and a function. It iterates over the values and calls the
	function with every element in the list. If the return of the function is equal to True, True is returned. If no
	element is found in the list that satisfies the function, False is returned. Better then the integrated any function
	because it stops when an element is found, the any function doesn't. Worst case scenario is that we take O(n) time.
	"""
	for x in formulas:
		if funct(x):
			return True
	return False

def extract_variables(p):
	"""
	Extracts all of the variables that occur in the specified formula, removes the duplicates and sorts the result.
	"""
	def local_extract_variables(p):
		"""
		Extracts all of the variables that occur in the specified formula and removes the duplicates.
		"""
		if isinstance(p, bf.Tru) or isinstance(p, bf.Fls):
			return []
		elif isinstance(p, bf.Not):
			return local_extract_variables(p.formula)
		elif isinstance(p, bf.Or) or isinstance(p, bf.And):
			return remove_duplicates(sum(map(lambda x: local_extract_variables(x), p.formulas), []))
		elif isinstance(p, bf.Var):
			return [p.name]
	return sorted(local_extract_variables(p))

def remove_duplicates(lst):
	"""
	Returns a sorted copy of the specified list that contains no duplicates.
	"""
	return [x for x, _ in itertools.groupby(sorted(lst))]

def pure_variables(cnf_formula):
	"""
	Checks for pure variables in CNF formula and returns appropriate assigned values
	"""
	if isinstance(cnf_formula, bf.Tru) or isinstance(cnf_formula, bf.Fls) or isinstance(cnf_formula, bf.Var) or isinstance(cnf_formula, bf.Not):
		return {}

	pure_variable_list = []
	not_pure = []
	for clause_OR in cnf_formula.formulas:
		for var in clause_OR.formulas:
			if isinstance(var, bf.Var):
				if bf.Not(var) in pure_variable_list:
					pure_variable_list.remove(bf.Not(var))
					not_pure.append(var.name)
				elif var.name not in not_pure and var not in pure_variable_list:
					pure_variable_list.append(var)
			elif isinstance(var, bf.Not):
				if var.formula in pure_variable_list:
					pure_variable_list.remove(var.formula)
					not_pure.append(var.formula.name)
				elif var.formula.name not in not_pure and var not in pure_variable_list:
					pure_variable_list.append(var)
	# Assign values to pure variables
	values = {}
	for pure_variable in pure_variable_list:
		if isinstance(pure_variable, bf.Var):
			values[pure_variable.name] = bf.Tru()
		elif isinstance(pure_variable, bf.Not):
			values[pure_variable.formula.name] = bf.Fls()
	return values
