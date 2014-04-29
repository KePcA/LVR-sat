"""
Basic examples of using the boolean formulas, algorithm utilities and DPLL
"""

__author__ = 'Grega'

import SAT_implementation.bool_formulas as bf
import SAT_implementation.algorithm_utilities as au

# True
bf.Tru()

# False
bf.Fls()

# Variable
x1 = bf.Var("x1")
x2 = bf.Var("x2")
x3 = bf.Var("x3")
x4 = bf.Var("x4")

# Not
n1 = bf.Not(bf.Tru())                                       # this is equivalent to bf.Fls()
n2 = bf.Not(bf.Fls())                                       # this is equivalent to bf.Tru()
n3 = bf.Not(x1)
n1 = bf.Not(bf.And([x1, x2, x3, x4]))
n2 = bf.Not(bf.Or([x1, x2, x3, x4]))

# And
and1 = bf.And([x1, x2, x3, x4])
and2 = bf.And([x1, bf.And([x1, x2, x3, x4]), x4, x3, x2])   # this is equivalent to bf.And([x1, x1, x2, x3, x4, x4, x3, x2])
and3 = bf.And([])                                           # bf.And([]) is equivalent to bf.Tru()

# Or
or1 = bf.Or([x1, x2, x3, x4])
or2 = bf.Or([x1, bf.Or([x1, x2, x3, x4]), x4, x3, x2])      # this is equivalent to bf.Or([x1, x1, x2, x3, x4, x4, x3, x2])
or3 = bf.Or([])                                             # bf.Or([]) is equivalent to bf.Fls()

# Examples of using the nnf method
print "NNF EXAMPLES:"
print au.nnf(bf.Not(bf.Not(bf.Var("b"))))
print au.nnf(bf.Or([bf.And([bf.Var("a"), bf.Var("b")]), bf.Var("c")]))
print au.nnf(bf.Not(bf.Or([bf.Var("a"), bf.Var("b")])))
print au.nnf(bf.And([bf.Var("a"), bf.And([bf.Var("b"), bf.Var("a")]), bf.Or([bf.Var("c"), bf.Var("b")])]))
print "-----------------------------------------------------------------------------------------------------------------\n"

# Examples of using the cnf method
print "CNF EXAMPLES:"
print au.cnf_nnf(bf.Or([bf.Var("b"), bf.Var("c")]))
print au.cnf_nnf(bf.And([bf.Not(bf.Var("a")), bf.Or([bf.Var("b"), bf.Var("c")])]))
print au.cnf_nnf(bf.And([bf.Var("a"), bf.Or([bf.Var("b"), bf.And([bf.Var("c"), bf.Var("d")])])]))
print au.cnf_nnf(bf.Not(bf.Or([bf.Var("a"), bf.Var("b"), bf.Not(bf.Fls())])))
print "-----------------------------------------------------------------------------------------------------------------\n"

# Examples of using the simplify method
print "SIMPLIFY EXAMPLES:"
print au.simplify(bf.Not(bf.Or([bf.Var("b"), bf.Var("c")])))
print au.simplify(bf.And([bf.Not(bf.Var("a")), bf.Or([bf.Var("b"), bf.Var("c")])]))
print au.simplify(bf.And([bf.Var("a"), bf.Or([bf.Var("b"), bf.Tru(), bf.And([bf.Fls(), bf.Var("c"), bf.Var("d")])])]))
print au.simplify(bf.Not(bf.Or([bf.Var("a"), bf.Var("b"), bf.Not(bf.Fls())])))
print "-----------------------------------------------------------------------------------------------------------------\n"

