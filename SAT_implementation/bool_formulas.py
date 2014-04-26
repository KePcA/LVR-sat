#coding:utf-8

"""
Implementacija razredov za predstavitev Boolovih formul
"""


############## Class for representation of FALSE ########################
class Fls():

	def __init__(self):
		pass

	def __repr__(self):
		return "F"

	def __eq__(self, other):
		return isinstance(other, Fls)

	def evaluate(self, dict):
		return False

	def replace(self, dict):
		"""
		Nothing to replace.
		"""
		return self


############## Class for representation of TRUE ########################
class Tru():

	def __init__(self):
		pass

	def __repr__(self):
		return "T"

	def __eq__(self, other):
		return isinstance(other, Tru)

	def evaluate(self, dict):
		return True

	def replace(self, dict):
		"""
		Nothing to replace.
		"""
		return self


############## Class for representation of VARIABLE ########################
class Var:

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name

	def __eq__(self, other):
		return isinstance(other, Var) and other.name == self.name

	#Value of the variable is obtained from the dictionary (dict) in which values of all the variables are stored, if exists.
	def evaluate(self, dict):
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


############## Class for representation of NEGATION ########################
class Not():

	def __init__(self, formula):
		self.formula = formula

	#For string representation we add ¬ in front of out formula we negate.
	def __repr__(self):
		return "¬" + repr(self.formula)

	def __eq__(self, other):
		return isinstance(other, Not) and self.formula == other.formula

	#We return the negation of our formula which value we get from the dictionary of variables' values (dict).
	def evaluate(self, dict):
		return not self.formula.evaluate(dict)

	def replace(self, dict):
		"""
		Replaces all of the occurrences of the Vars that are represented by the keys in the values dictionary with the
		value located in the dictionary (key - name of Var, value - value of Var). If a Var with the name isn't defined
		with a key in the dictionary, the Var isn't replaced.
		"""
		return Not(self.formula.replace(dict))



############## Class for representation of AND ########################
class And():

	#Argument formulas represents list of formulas which are combined to a single formula by conjunctions.
	def __init__(self, formulas):
		self.formulas = formulas

	def __repr__(self):
		string = ""
		for i in xrange(len(self.formulas) - 1):
			string += repr(self.formulas[i])
			string += " ^ "
		string += repr(self.formulas[len(self.formulas) - 1])
		return "(" + string + ")"

	def __eq__(self, other):
		return isinstance(other, And) and self.formulas == other.formulas

	#Method returns conjunction of values of all the formulas being present in the list. We stop as soon as one of the formula is false.
	def evaluate(self, dict):
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

	#If conjunction contains no variables
	def isEmpty(self):
		if self.formulas:
			return False
		else:
			return True

############## Class for representation of OR ########################
class Or():

	#Argument formulas represents list of formulas which are combined to a single formula by disjunctions.
	def __init__(self, formulas):
		self.formulas = formulas

	def __repr__(self):
		string = ""
		for i in xrange(len(self.formulas) - 1):
			string += repr(self.formulas[i])
			string += " ∨ "
		string += repr(self.formulas[len(self.formulas) - 1])
		return "(" + string + ")"

	def __eq__(self, other):
		return isinstance(other, Or) and self.formulas == other.formulas

	#Method returns disjunction of values of all the formulas being present in the list. We stop as soon as one of the formula is true.
	def evaluate(self, dict):
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

	#If disjunction contains no variables
	def isEmpty(self):
		if self.formulas:
			return False
		else:
			return True
