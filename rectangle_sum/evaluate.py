from turingarena import *

import random
import sys

value_range = range(10, 99)

algorithm = submitted_algorithm()


def main():
    bilinear = True
    for size in (10,30,100):
        m = n = size
        bilinear &= evaluate_case(
            m, n, r1=m//4, r2=3*m//4, c1=n//4, c2=3*n//4, time_limit=0.1)
        bilinear &= evaluate_case_limits(m, n, time_limit=0.1)

    monolinear = bilinear
    for size in (10,30,100):
        m = n = size
        monolinear &= evaluate_case(m, n, r1=m//4, r2=3*m//4,
                                    c1=n//4, c2=3*n//4, time_limit=0.005)
        monolinear &= evaluate_case_limits(m, n, time_limit=0.005)

    sublinear = monolinear
    sublinear &= evaluate_case(100, 100, r1=10, r2=90,
                               c1=10, c2=90, time_limit=0.0001)

    evaluation_result(goals=dict(
        bilinear=bilinear,
        monolinear=monolinear,
        sublinear=sublinear,
    ))


def evaluate_case(m, n, r1, r2, c1, c2, time_limit):
    print("evaluate_case", m, n, r1, r2, c1, c2, time_limit, file=sys.stderr)
    mat = [[random.choice(value_range) for _ in range(n)] for _ in range(m)]
    try:
        with algorithm.run() as process:
            process.call.get_matrix(len(mat), len(mat[0]), mat)
            with process.section(time_limit=time_limit):
                risp = process.call.rectangle_sum(r1, r2, c1, c2)
    except TimeLimitExceeded:
        print ("You take too much time to answer a query.")
        return False
    except AlgorithmRuntimeError as e:
        print("Error:", e)
        return False

    correct_risp = 0
    for i in range(r1, r2+1):
        correct_risp += sum(mat[i][c1:c2+1])

    if risp != correct_risp:
        print ("The sum value returned is not correct.")
        return False
    return True


def evaluate_case_limits(m, n, time_limit):
    return evaluate_case(m, n, r1=0, r2=m-1, c1=0, c2=n-1, time_limit=time_limit)


main()
