from turingarena.sandbox.exceptions import AlgorithmRuntimeError
import random
import sys

value_range = range(10, 99)

def evaluate(algorithm):
    goals = {}
    goals["bi-linear"] = (
        all(
            evaluate_case(algorithm, m, n, r1=m//4, r2=3*m//4, c1=n//4, c2=3*n//4, time_limit=0.1)
            for m in (10, 100, 1000)
               for n in (10, 100, 1000)
        )
    )
    goals["mono-linear"] = (
        goals["bi-linear"]
        and
        all(
            evaluate_case(algorithm, m, n, r1=m//4, r2=3*m//4, c1=n//4, c2=3*n//4, time_limit=0.005)
            for m in (10, 100, 1000)
               for n in (10, 100, 1000)
        )
    )
    goals["sublinear"] = (
        goals["bi-linear"]
        and
        goals["mono-linear"]
        and
        evaluate_case(algorithm, 5000, 5000, r1=127, r2=472, c1=126, c2=492, time_limit=0.0001)
        and
        evaluate_case_limits(algorithm, 5000, 5000, time_limit=0.0001)
    )

    return {"goals": goals}


def evaluate_case(algorithm, m, n, r1, r2, c1, c2, time_limit):
    mat = [ [ random.choice(value_range) for _ in range(n) ] for _ in range(m) ]
    try:
        risp = run(algorithm, mat, r1, r2, c1, c2, time_limit)
    except AlgorithmRuntimeError as e:
        print(n, time_limit, e, file=sys.stderr)
        print ("You take too much time to answer a query.")
        return False
    correct_risp = 0;
    for i in range(m):
        correct_risp += sum(mat[i][c1:c2+1])
    if risp != correct_risp:
        print ("The sum value returned is not correct.")
        return False
    return True

def evaluate_case_limits(algorithm, m, n, time_limit):
    return evaluate_case(algorithm, m, n, r1=0, r2=m, c1=0, c2=n, time_limit=time_limit)   

def run(algorithm, mat, r1, r2, c1, c2, time_limit):
    with algorithm.run() as process:
        process.call.get_matrix(len(mat), len(mat[0]), mat)
        with process.section(time_limit=time_limit):
            return process.call.matrix_sum(r1, r2, c1, c2)
