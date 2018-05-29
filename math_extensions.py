from itertools import combinations, chain, product


def powerset(iterable):
    xs = list(iterable)
    return [list(interpretation) for interpretation in
            chain.from_iterable(combinations(xs, n) for n in range(len(xs) + 1))]


def get_all_interpretations(params):
    for interpretation in product([False, True], repeat=len(params)):
        yield {param: value for param, value in zip(params, interpretation)}


def convert_truth_table_to_list(truth_table, result=None):
    return [[int(val) for key, val in interpretation.items()] for interpretation, value in
            truth_table if value is result]
