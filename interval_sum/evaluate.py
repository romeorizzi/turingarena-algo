from turingarena import *

import random
import sys

value_range = range(10, 99)

algorithm = submitted_algorithm()


def main():
    linear = True
    #for n in (10, 100, 1000, 10**4, 10**5, 10**6):
    for n in (10, 100, 1000):
        linear &= evaluate_case(algorithm, n, a=n//4, b=3*n//4, time_limit=0.1)

    sublinear = linear
    #sublinear &= evaluate_case(algorithm, 10**6, a=127, b=10**3, time_limit=0.0001)
    sublinear &= evaluate_case(algorithm, 100, a=10, b=80, time_limit=0.0001)

    evaluation_result(goals=dict(
        linear=linear,
        sublinear=sublinear,
    ))


def evaluate_case(algorithm, n, a, b, time_limit):
    vals = [random.choice(value_range) for _ in range(n)]
    try:
        with algorithm.run() as process:
            process.call.get_sequence(len(vals), vals)
            with process.section(time_limit=time_limit):
                risp = process.call.interval_sum(a, b)
    except TimeLimitExceeded:
        print ("You take too much time to answer a query.")
        return False
    except AlgorithmError as e:
        print("Error: ", e)
        return False
    if risp != sum(vals[a:b+1]):
        print ("The sum value returned is not correct.")
        return False
    return True


main()
