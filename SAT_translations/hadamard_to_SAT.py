#coding:utf-8

"""
Translation of hadamard problem to SAT problem
"""
from SAT_implementation import bool_formulas as bf


def hadamard_translation(n):
	"""
	Translates the hadamard problem of size n to a SAT problem.
	"""
	result = bf.And([])

	if n % 2 != 0:
		return bf.Fls()
	else:
		result.formulas.append(bf.Var("r0c0"))
		for i in range(1,n):
			result.formulas.append(bf.Var("r0c%d" % i))
			result.formulas.append(bf.Var("r%dc0" % i))

		for i in range(n):
			for j in range(i + 1, n):
				div = n//2
				result.formulas.append(bf.Var("r%dr%df%dn%d" % (i, j, n, div)))
				result.formulas.append(bf.Var("r%dr%df1n0" % (i, j)))
				result.formulas.append(bf.Not(bf.Var("r%dr%df1n1" % (i, j))))

				for k in range(1, n):
					p = bf.Var("r%dr%df%dn0" % (i, j, k+1))
					q1 = bf.Var("r%dr%df%dn0" % (i, j, k))
					q2_p = bf.Var("r%dc%d" % (i, k))
					q2_q = bf.Var("r%dc%d" % (j, k))
					q2 = bf.Or([bf.And([q2_p, q2_q]), bf.And([bf.Not(q2_p), bf.Not(q2_q)])])
					q = bf.And([q1, q2])
					result.formulas.append(bf.Or([bf.And([p, q]), bf.And([bf.Not(p), bf.Not(q)])]))

					if k < div:
						p = bf.Var("r%dr%df%dn%d" % (i, j, k+1, k+1))
						q1 = bf.Var("r%dr%df%dn%d" % (i, j, k, k))
						q2_p = bf.Var("r%dc%d" % (i, k))
						q2_q = bf.Var("r%dc%d" % (j, k))
						q2 = bf.Not(bf.Or([bf.And([q2_p, q2_q]), bf.And([bf.Not(q2_p), bf.Not(q2_q)])]))
						q = bf.And([q1, q2])
						result.formulas.append(bf.Or([bf.And([p, q]), bf.And([bf.Not(p), bf.Not(q)])]))

					for l in range(min(k, div)):
						p = bf.Var("r%dr%df%dn%d" % (i, j, k+1, l+1))
						q11 = bf.Var("r%dr%df%dn%d" % (i, j, k, l))
						q12_p = bf.Var("r%dc%d" % (i, k))
						q12_q = bf.Var("r%dc%d" % (j, k))
						q12 = bf.Not(bf.Or([bf.And([q12_p, q12_q]), bf.And([bf.Not(q12_p), bf.Not(q12_q)])]))
						q1 = bf.And([q11, q12])
						q21 = bf.Var("r%dr%df%dn%d" % (i, j, k, l+1))
						q22_p = bf.Var("r%dc%d" % (i, k))
						q22_q = bf.Var("r%dc%d" % (j, k))
						q22 = bf.Or([bf.And([q22_p, q22_q]), bf.And([bf.Not(q22_p), bf.Not(q22_q)])])
						q2 = bf.And([q21, q22])
						q = bf.Or([q1, q2])
						result.formulas.append(bf.Or([bf.And([p, q]), bf.And([bf.Not(p), bf.Not(q)])]))
		return result