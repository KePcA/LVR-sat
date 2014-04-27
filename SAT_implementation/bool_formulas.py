#coding:utf-8

"""
Implementation of classes for the representation of a Boolean formula.
"""

########################################## Class for representation of FALSE ###########################################
class Fls():

	def __init__(self):
		pass

	def __repr__(self):
		"""
		Representation of FALSE.
		"""
		return "F"

	def __eq__(self, other):
		"""
		Equality check.
		"""
		return isinstance(other, Fls)

	def evaluate(self, dict):
		"""
		Always evaluates to False.
		"""
		return False

	def replace(self, dict):
		"""
		Nothing to replace.
		"""
		return self


########################################### Class for representation of TRUE ###########################################
class Tru():

	def __init__(self):
		pass

	def __repr__(self):
		"""
		Representation of TRUE.
		"""
		return "T"

	def __eq__(self, other):
		"""
		Equality check.
		"""
		return isinstance(other, Tru)

	def evaluate(self, dict):
		"""
		Always evaluates to True.
		"""
		return True

	def replace(self, dict):
		"""
		Nothing to replace.
		"""
		return self


######################################### Class for representation of VARIABLE #########################################
class Var:

	def __init__(self, name):
		"""
		Argument is the name of the variable.
		"""
		self.name = name

	def __repr__(self):
		"""
		Representation of a VARIABLE.
		"""
		return self.name

	def __eq__(self, other):
		"""
		Equality check.
		"""
		return isinstance(other, Var) and other.name == self.name

	def evaluate(self, dict):
		"""
		Returns the variable contained in the specified dictionary or None if the variable doesn't exist.
		"""
		return dict.get(self.name).evaluate(dict)

	def replace(self, dict):
		"""
		Replaces all of the occurrences of the Vars that are represented by the keys in the values dictionary with the
		value located in the dictionary (key - name of Var, value - value of Var). If a Var with the name isn't defined
		with a key in the dictionary, the Var isn't replaced.
		"""
		value = dict.get(self.name)
		if value is None:
			return self
		else:
			return value


######################################### Class for representation of NEGATION #########################################
class Not():

	def __init__(self, formula):
		"""
		Argument is a representation of another boolean formula.
		"""
		self.formula = formula

	def __repr__(self):
		"""
		Representation of NOT.
		"""
		return "¬" + repr(self.formula)

	def __eq__(self, other):
		"""
		Equality check.
		"""
		return isinstance(other, Not) and self.formula == other.formula

	def evaluate(self, dict):
		"""
		Returns the negation of our formula which value we get from the dictionary of variables' values (dict).
		"""
		return not self.formula.evaluate(dict)

	def replace(self, dict):
		"""
		Replaces all of the occurrences of the Vars that are represented by the keys in the values dictionary with the
		value located in the dictionary (key - name of Var, value - value of Var). If a Var with the name isn't defined
		with a key in the dictionary, the Var isn't replaced.
		"""
		return Not(self.formula.replace(dict))

########################################### Class for representation of AND ############################################
class And():

	def __init__(self, formulas):
		"""
		Argument formulas represents list of formulas which are combined to a single formula by conjunctions.
		"""
		self.formulas = formulas

	def __repr__(self):
		"""
		Representation of AND.
		"""
		string = ""
		for i in xrange(len(self.formulas) - 1):
			string += repr(self.formulas[i])
			string += " ^ "
		string += repr(self.formulas[len(self.formulas) - 1])
		return "(" + string + ")"

	def __eq__(self, other):
		"""
		Equality check.
		"""
		return isinstance(other, And) and self.formulas == other.formulas

	def evaluate(self, dict):
		"""
		Returns the conjunction of values of all the formulas being present in the list. We stop as soon as one of the formula is false.
		"""
		for formula in self.formulas:
			if formula.evaluate(dict) is False:
				return False
		return True

	def replace(self, dict):
		"""
		Replaces all of the occurrences of the Vars that are represented by the keys in the values dictionary with the
		value located in the dictionary (key - name of Var, value - value of Var). If a Var with the name isn't defined
		with a key in the dictionary, the Var isn't replaced.
		"""
		return And([x.replace(dict) for x in self.formulas])

	def isEmpty(self):
		"""
		If conjunction contains no variables
		"""
		if self.formulas:
			return False
		else:
			return True

############################################ Class for representation of OR ############################################
class Or():

	def __init__(self, formulas):
		"""
		Argument formulas represents list of formulas which are combined to a single formula by disjunctions.
		"""
		self.formulas = formulas

	def __repr__(self):
		"""
		Representation of OR.
		"""
		string = ""
		for i in xrange(len(self.formulas) - 1):
			string += repr(self.formulas[i])
			string += " ∨ "
		string += repr(self.formulas[len(self.formulas) - 1])
		return "(" + string + ")"

	def __eq__(self, other):
		"""
		Equality check.
		"""
		return isinstance(other, Or) and self.formulas == other.formulas

	def evaluate(self, dict):
		"""
		Returns the disjunction of values of all the formulas being present in the list. We stop as soon as one of the formula is true.
		"""
		for formula in self.formulas:
			if formula.evaluate(dict) is True:
				return True
		return False

	def replace(self, dict):
		"""
		Replaces all of the occurrences of the Vars that are represented by the keys in the values dictionary with the
		value located in the dictionary (key - name of Var, value - value of Var). If a Var with the name isn't defined
		with a key in the dictionary, the Var isn't replaced.
		"""
		return Or([x.replace(dict) for x in self.formulas])

	def isEmpty(self):
		"""
		If disjunction contains no variables
		"""
		if self.formulas:
			return False
		else:
			return True
