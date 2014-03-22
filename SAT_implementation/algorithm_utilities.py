import bool_formulas as bf


def cnf_nnf(p):
	"""
	Converts the specified p formula to a NNF form and then to a CNF form.
	"""
	return cnf(nnf(p))


def cnf(p):
	"""
	Converts the specified p formula to a CNF form.
	"""
	if isinstance(p, bf.And):
		return flatten(bf.And([cnf(x) for x in p.formulas]))
	elif isinstance(p, bf.Or):
		f_length = len(p.formulas)
		if f_length == 0:
			return bf.Fls()
		elif f_length == 1:
			return cnf(p.formulas[0])
		else:
			flattened = flatten(p)
			if isinstance(flattened, bf.Or) or isinstance(flattened, bf.And):
				flattened_cnf = [cnf(x) for x in flattened.formulas]
				conjunctions = [x for x in flattened_cnf if isinstance(x, bf.And)]
				disjunctions = [x for x in flattened_cnf if not isinstance(x, bf.And)]
				if len(flattened_cnf) == len(disjunctions):
					return bf.Or(disjunctions)
				else:
					return flatten(bf.And([cnf(bf.Or([x] + disjunctions + conjunctions[1:])) for x in conjunctions[0].formulas]))
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
			# Get rid of not, return the flattened formula.
			return flatten(x.formula)
		elif isinstance(x, bf.Or):
			# Convert to And(Not(y1), ...,Not(yn)) and flatten the formula.
			return flatten(bf.And([bf.Not(y) for y in x.formulas]))
		elif isinstance(x, bf.And):
			# Convert to Or(Not(y1), ...,Not(yn)) and flatten the formula.
			return flatten(bf.Or([bf.Not(y) for y in x.formulas]))
		else:
			return p
	elif isinstance(p, bf.Or):
		flattened = [flatten(x) for x in p.formulas]
		length = len(flattened)
		if length == 0:
			return bf.Fls()
		elif length == 1:
			return flattened[0]
		else:
			formulas = sum([x.formulas if isinstance(x, bf.Or) else [x] for x in flattened], [])
			if __any(formulas, lambda x: isinstance(x, bf.Tru)):
				return bf.Tru()
			else:
				return bf.Or(formulas)
	elif isinstance(p, bf.And):
		flattened = [flatten(x) for x in p.formulas]
		length = len(flattened)
		if length == 0:
			return bf.Tru()
		elif length == 1:
			return flattened[0]
		else:
			formulas = sum([x.formulas if isinstance(x, bf.And) else [x] for x in flattened], [])
			if __any(formulas, lambda x: isinstance(x, bf.Fls)):
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


def simplify(p):
	"""
	Simplified the specified p formula.
	"""
	if (isinstance(p, bf.Tru)) or isinstance(p, bf.Fls) or isinstance(p, bf.Var):
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
			return simplify(x.formula)
		elif isinstance(x, bf.Or):
			# Or(y1,...,yn) -> And(Not(y1),...Not(yn))
			return simplify(bf.And([bf.Not(y) for y in x.formulas]))
		elif isinstance(x, bf.And):
			# And(y1,...,yn) -> Or(Not(y1),...Not(yn))
			return simplify(bf.Or([bf.Not(y) for y in x.formulas]))
	elif isinstance(p, bf.Or):
		# Simplify sub-formulas
		simplified = map(simplify, p.formulas)
		# Merge and remove duplicates.
		formulas = remove_duplicates(sum([x.formulas if isinstance(x, bf.Or) else [x] for x in simplified], []))
		length = len(formulas)
		if length == 0:
			return bf.Fls()
		if length == 1:
			return formulas[0]
		else:
			# Find all of the or absorptions
			absorption, absorption_tuples = __find_absorptions(formulas, bf.And)
			# Remove all of the absorptions
			formulas = filter(lambda x: x not in absorption, formulas)
			# Extend the list wit new absorptions
			formulas.extend([simplify(bf.Or([z for z in x.formulas if z not in y])) for x, y in absorption_tuples])
			# Remove duplicates
			formulas = remove_duplicates(formulas)
			# Remove all falses
			formulas = filter(lambda x: not isinstance(x, bf.Fls), formulas)
			# If one is true, true must be returned.
			if __any(formulas, lambda x: isinstance(x, bf.Tru)):
				return bf.Tru()
			# If there is an element x that is equal to Not and the value of Not is also contained in the formulas return true
			if __any(formulas, lambda x: isinstance(x, bf.Not) and x.formula in formulas):
					return bf.Tru()
			# Recheck current length of formulas
			length = len(formulas)
			if length == 0:
				return bf.Tru()
			if length == 1:
				return formulas[0]
			else:
				return bf.Or(sorted(formulas))
	elif isinstance(p, bf.And):
		# Simplify sub-formulas
		simplified = map(simplify, p.formulas)
		# Merge and remove duplicates.
		formulas = remove_duplicates(sum([x.formulas if isinstance(x, bf.And) else [x] for x in simplified], []))
		length = len(formulas)
		if length == 0:
			return bf.Tru()
		if length == 1:
			return formulas[0]
		else:
			# Find all of the and absorptions
			absorption, absorption_tuples = __find_absorptions(formulas, bf.Or)
			# Remove all of the absorptions
			formulas = filter(lambda x: x not in absorption, formulas)
			# Extend the list wit new absorptions
			formulas.extend([simplify(bf.Or([z for z in x.formulas if z not in y])) for x, y in absorption_tuples])
			# Remove duplicates
			formulas = remove_duplicates(formulas)
			# Remove all trues
			formulas = filter(lambda x: not isinstance(x, bf.Tru), formulas)
			# If one is false, false must be returned.
			if __any(formulas, lambda x: isinstance(x, bf.Fls)):
				return bf.Fls()
			# If there is an element x that is equal to Not and the value of Not is also contained in the formulas return false
			if __any(formulas, lambda x: isinstance(x, bf.Not) and x.formula in formulas):
				return bf.Fls()
			# Recheck current length of formulas
			length = len(formulas)
			if length == 0:
				return bf.Tru()
			if length == 1:
				return formulas[0]
			else:
				return bf.And(sorted(formulas))


def __find_absorptions(lst, class_value):
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


def __any(formulas, funct):
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

def remove_duplicates(lst):
	"""
	Removes the duplicates from the specified list.
	"""
	return [lst[i] for i, x in enumerate(lst) if x not in lst[i + 1:]]