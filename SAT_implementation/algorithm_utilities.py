import bool_formulas as bf


def cnf(p):
	if isinstance(p, bf.And):
		return flatten(bf.And([cnf(x) for x in p.formulas]))
	elif isinstance(p, bf.Or):
		f_length = len(p.formulas)
		if f_length == 0:
			return p
		elif f_length == 1:
			return p.formulas[0]
		q = flatten(p)
		cnf_q = [cnf(x) for x in q]
		ands = [x for x in cnf_q if isinstance(x, bf.And)]
		if len(cnf_q) == len(ands):
			return bf.And(ands)
		else:
			others = [x for x in cnf_q if not isinstance(x, bf.And)]
			return flatten(bf.And([cnf(bf.Or(ands + [x] + others[:1])) for x in others[0].formulas]))
	else:
		return p


def flatten(p):
	if isinstance(p, bf.Tru) or isinstance(p, bf.Fls) or isinstance(p, bf.Var):
		return p
	if isinstance(p, bf.Not):
		x = p.formula
		if isinstance(x, bf.Not):
			return x
		elif isinstance(x, bf.Or):
			return flatten(bf.And(bf.Not(y) for y in x.formulas))
		elif isinstance(x, bf.And):
			return flatten(bf.Or(bf.Not(y) for y in x.formulas))
		else:
			return p
	elif isinstance(p, bf.Or):
		if len(p.formulas) == 1:
			return flatten(p.formulas[0])
		else:
			neq_formula = sum([y.formulas if isinstance(y, bf.Or) else [y] for y in [flatten(x) for x in p.formulas]], [])
			if any([isinstance(x, bf.And) and len(x.formulas) == 0 for x in neq_formula]):
				return bf.Tru()
			else:
				return bf.Or(neq_formula)
	elif isinstance(p, bf.And):
		if len(p.formulas) == 1:
			return flatten(p.formulas[0])
		else:
			n_formula = sum([y.formulas if isinstance(y, bf.And) else [y] for y in [flatten(x) for x in p.formulas]], [])
			if any([isinstance(x, bf.Or) and len(x.formulas) == 0 for x in n_formula]):
				return bf.Fls()
			else:
				return bf.And(n_formula)


def nnf(p):
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
		# TODO: needs to be implemented
		print("NOT IMPLEMENTED YET!")
	elif isinstance(p, bf.And):
		# TODO: needs to be implemented
		print("NOT IMPLEMENTED YET!")


def evaluate(values, p):
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