import bool_formulas as bf


def cnf(p):
	"""
	Converts the specified p formula to a CNF form.
	"""
	if isinstance(p, bf.And):
		return flatten(bf.And([cnf(x) for x in p.formulas]))
	elif isinstance(p, bf.Or):
		f_length = len(p.formulas)
		if f_length == 0:
			return bf.Fls
		elif f_length == 1:
			return p.formulas[0]
		else:
			flattened = flatten(p)
			flattened_cnf = [cnf(x) for x in flattened]
			ands = [x for x in flattened_cnf if isinstance(x, bf.And)]
			if len(flattened_cnf) == len(ands):
				return bf.And(ands)
			else:
				others = [x for x in flattened_cnf if not isinstance(x, bf.And)]
				return flatten(bf.And([cnf(bf.Or(ands + [x] + others[:1])) for x in others[0].formulas]))
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
			return flatten(bf.And(bf.Not(y) for y in x.formulas))
		elif isinstance(x, bf.And):
			# Convert to Or(Not(y1), ...,Not(yn)) and flatten the formula.
			return flatten(bf.Or(bf.Not(y) for y in x.formulas))
		else:
			return p
	elif isinstance(p, bf.Or):
		flattened = [flatten(x) for x in p.formulas]
		length = len(flattened)
		if length == 0:
			return bf.Fls
		elif length == 1:
			return flattened[0]
		else:
			formulas = sum([x.formulas if isinstance(x, bf.Or) else [x] for x in flattened], [])
			if any([isinstance(x, bf.And) and len(x.formulas) == 0 for x in formulas]):
				return bf.Tru()
			else:
				return bf.Or(formulas)
	elif isinstance(p, bf.And):
		flattened = [flatten(x) for x in p.formulas]
		length = len(flattened)
		if length == 0:
			return bf.Tru
		elif length == 1:
			return flattened[0]
		else:
			formulas = sum([x.formulas if isinstance(x, bf.And) else [x] for x in flattened], [])
			if any([isinstance(x, bf.Or) and len(x.formulas) == 0 for x in formulas]):
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
			return bf.And([nnf(bf.Not(y)) for y in x.formulas])
		elif isinstance(x, bf.And):
			return bf.Or([nnf(bf.Not(y)) for y in x.formulas])
	elif isinstance(p, bf.Or):
			return bf.Or([nnf(x) for x in p.formulas])
	elif isinstance(p, bf.And):
			return bf.And([nnf(x) for x in p.formulas])


def simplify(p):
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
			return simplify(x.formula)
		elif isinstance(x, bf.Or):
			return simplify(bf.And([bf.Not(y) for y in x.formulas]))
		elif isinstance(x, bf.And):
			return simplify(bf.Or([bf.Not(y) for y in x.formulas]))
	elif isinstance(p, bf.Or):
		simplified = [simplify(x) for x in p.formulas]
		formulas = set(sum([x.formulas if isinstance(x, bf.Or) else [x] for x in simplified], []))
		length = len(formulas)
		if length == 0:
			return bf.Fls
		if length == 1:
			return formulas[0]
		else:
			# TODO: needs to be implemented
			return bf.Or(sorted(formulas))
	elif isinstance(p, bf.And):
		simplified = [simplify(x) for x in p.formulas]
		formulas = set(sum([x.formulas if isinstance(x, bf.And) else [x] for x in simplified], []))
		length = len(formulas)
		if length == 0:
			return bf.Tru
		if length == 1:
			return formulas[0]
		else:
			# TODO: needs to be implemented
			return bf.And(sorted(formulas))


def evaluate(values, p):
	"""
	Evaluate the specified p formula with the specified values.
	"""
	if isinstance(p, bf.Tru) or isinstance(p, bf.Fls):
		return p.evaluate()
	elif isinstance(p, bf.Var):
		return p.evaluate(values)
	elif isinstance(p, bf.Not):
		return not evaluate(values, p.formula)
	elif isinstance(p, bf.Or):
		for x in p.formulas:
			if evaluate(values, x) is True:
				return True
		return False
	elif isinstance(p, bf.And):
		for x in p.formulas:
			if evaluate(values, x) is False:
				return False
		return True