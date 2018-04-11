from turingarena.sandbox.exceptions import AlgorithmRuntimeError
import random
import sys

value_range = range(10, 99)

def evaluate(algorithm):
    goals = {}
    goals["linear"] = (
        all(
            evaluate_case(algorithm, n, a=n//4, b=3*n//4, time_limit=0.1)
            for n in (10, 100, 1000, 10**4)
        )
    )
    goals["sublinear"] = (
        goals["linear"]
        and
        evaluate_case(algorithm, 10**4, a=127, b=10**3, time_limit=0.00001)
    )

    return {"goals": goals}


def evaluate_case(algorithm, n, a, b, time_limit):
    vals = [ random.choice(value_range) for _ in range(n) ]
    try:
        risp = run(algorithm, vals, a, b, time_limit)
    except AlgorithmRuntimeError as e:
        print(n, time_limit, e, file=sys.stderr)
        return False
        if risp != sum(vals[a:b+1]):
            return False
    return True


def run(algorithm, vals, a, b, time_limit):
    with algorithm.run() as process:
        process.call.get_sequence(len(vals), vals)
        with process.section(time_limit=time_limit):
            return process.call.interval_sum(a,b)
