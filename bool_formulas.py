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
        return type(other)==Fls

    def valuate(self):
        return False




############## Class for representation of TRUE ########################
class Tru():

    def __init__(self):
        pass

    def __repr__(self):
        return "T"

    def __eq__(self, other):
        return type(other)==Fls

    def valuate(self):
        return True


############## Class for representation of VARIABLE ########################
class Var:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return type(other)==Var and other.name==self.name

    #Value of the variable is obtained from the dictionary (dict) in which values of all the variables are stored, if exists.
    def valuate(self, dict):
        return dict[self.name]


############## Class for representation of NEGATION ########################
class Not():

    def __init__(self, formula):
        self.formula = formula

    #For string representation we add ¬ in front of out formula we negate.
    def __repr__(self):
        return "¬"+repr(self.formula)

    def __eq__(self, other):
        return type(other)==Not and self.formula==other.formula

    #We return the negation of our formula which value we get from the dictionary of variables' values (dict).
    def valuate(self, dict):
        return not self.formula.valuate(dict)



############## Class for representation of AND ########################
class And():

    #Argument formulas represents list of formulas which are combined to a single formula by conjunctions.
    def __init__(self, formulas):
        self.formulas = formulas

    def __repr__(self):
        string = ""
        for formula in self.formulas:
            string += " ∧ "+repr(formula)
        return "("+string[5:]+")"

    def __eq__(self, other):
        return type(other)==And and self.formulas==other.formulas

    #Method returns conjunction of values of all the formulas being present in the list. We stop as soon as one of the formula is false.
    def valuate(self, dict):
        value = True
        for formula in self.formulas:
            value = value and formula.valuate(dict)
            if not value:
                return False
        return True

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
        for formula in self.formulas:
            string += " ∨ "+repr(formula)
        return "("+string[5:]+")"

    def __eq__(self, other):
        return type(other)==Or and self.formulas==other.formulas

    #Method returns disjunction of values of all the formulas being present in the list. We stop as soon as one of the formula is true.
    def valuate(self, dict):
        value = False
        for formula in self.formulas:
            value = value or formula.valuate(dict)
            if value:
                return True
        return False

    #If disjunction contains no variables
    def isEmpty(self):
        if self.formulas:
            return False
        else:
            return True



"""
variable_dictionary = {"q": True, "p": False, "r": True}

q = Var("q")
p = Var("p")
r = Var("r")

formula = Not(Or([And([Not(q), p, r]), Not(Or([q,Not(p),Tru()]))]))
print formula.__repr__()
print formula.valuate(variable_dictionary)
"""