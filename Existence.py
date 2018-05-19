from collections import defaultdict

from sympy import sympify, to_dnf, to_cnf, satisfiable
from sympy.abc import F, X, Y
import sympy


def existence(expression):
    cnf = to_cnf(sympify(expression), True)
    symbols = cnf.atoms()
    symbols.remove(F)
    print(cnf)
    print(get_zero_interpretation(symbols))
    print(cnf.subs(get_zero_interpretation(symbols)))
    if satisfiable(cnf):
        return True
    else:
        return False


def find_all_solutions(expression):
    dnf = to_dnf(sympify(expression))
    symbols = dnf.atoms()
    if F not in symbols:
        return 0
    print(dnf.subs(F, 0))


def get_params(n):
    result = ''
    for i in range(n):
        result += 'x' + str(i + 1) + ' '
    return sympy.symbols(result)


def get_zero_interpretation(params):
    return {i : 0 for i in params}


expr = '(x1&x2)>>(F|x3)'
false = '((F|Y)>>~X)>>(F&X)'
print(existence(false))
