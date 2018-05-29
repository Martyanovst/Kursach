from sympy import sympify, to_cnf, Or, And
from sympy.abc import F

from math_extensions import *


def existence(expression):
    cnf = to_cnf(sympify(expression), True)
    symbols = cnf.atoms()
    symbols.remove(F)
    for interpretation in get_all_interpretations(symbols):
        if not cnf.subs(interpretation):
            return False
    return True


def find_all_solutions(expression):
    cnf = to_cnf(sympify(expression), True)
    symbols = cnf.atoms()
    symbols.remove(F)
    print(cnf)
    truth_table = []
    for interpretation in get_all_interpretations(symbols):
        formula = cnf.subs(interpretation)
        if not formula:
            return False
        elif formula == F:
            truth_table.append((interpretation, True))
        elif formula == ~F:
            truth_table.append((interpretation, False))
        else:
            truth_table.append((interpretation, None))
    return get_all_full_dnf(truth_table, symbols)


def get_all_full_dnf(truth_table, params):
    minterms = convert_truth_table_to_list(truth_table, True)
    specific = convert_truth_table_to_list(truth_table)
    for interpretation in powerset(specific):
        yield to_full_dnf(minterms + interpretation, params)


def to_full_dnf(minterms, params):
    result = False
    list_of_params = list(params)
    for term in minterms:
        component = True
        for i in range(len(list_of_params)):
            if term[i]:
                component = And(component, list_of_params[i])
            else:
                component = And(component, ~list_of_params[i])
        result = Or(result, component)
    return result


expr = '(X&Y)>>(F|Z)'
false = '((F|Y)>>~X)>>(F&X)'
if existence(false):
    for solution in find_all_solutions(expr):
        print(solution)
else:
    print("Unsatisfied")
