# brute force solution that solves wwwdot - google = dotcom
# Zenith @ Rock Stone . me
# Remark: if "e" == "m", the solution is unique: 555378 - 177104 = 378274

from constraint import *

problem = Problem()

problem.addVariables(["c", "d", "e", "g", "l", "m", "o", "t", "w"], range(10))
problem.addConstraint(AllDifferentConstraint())
problem.addConstraint(lambda d, g, w: d != 0 and g != 0 and w != 0, ("d", "g", "w"))
problem.addConstraint(lambda c, d, e, g, l, m, o, t, w:
                      (10 ** 5 * g + 10 ** 4 * o + 10 ** 3 * o + 10 ** 2 * g + 10 * l + e)
                    + (10 ** 5 * d + 10 ** 4 * o + 10 ** 3 * t + 10 ** 2 * c + 10 * o + m)
                   == (10 ** 5 * w + 10 ** 4 * w + 10 ** 3 * w + 10 ** 2 * d + 10 * o + t),
                      ("c", "d", "e", "g", "l", "m", "o", "t", "w"))
solution = problem.getSolutions()
print solution
