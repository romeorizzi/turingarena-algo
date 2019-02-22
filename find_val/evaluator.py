from turingarena import *

import random
import sys

value_range = range(10**8, 10**9)

algorithm = submitted_algorithm()


def main():
    linear = True

    for n in (10, 100, 1000):
        linear &= evaluate_case(n, True, time_limit=0.1)
        linear &= evaluate_case(n, False, time_limit=0.1)

    sublinear = linear
    for n in (10000,):
        sublinear &= evaluate_case(n, True, time_limit=0.0001)
        sublinear &= evaluate_case(n, False, time_limit=0.0001)

    evaluation_result(goals=dict(
        linear=linear,
        sublinear=sublinear,
    ))


def evaluate_case(n, present, time_limit):
    vals = random.choices(value_range, k=n)

    val = random.choice(vals)
    if not present:
        while val in vals:
            val = random.choice(value_range)

    try:
        with algorithm.run() as process:
            process.call.store_list(len(vals), vals)
            with process.section(time_limit=time_limit):
                index = process.call.find_val(val)
    except AlgorithmError as e:
        print(n, time_limit, e, file=sys.stderr)
        return False
        
    if vals[index] == val:
        return True
    if not present and index == -1:
        return True
    return False


main()
