from turingarena.sandbox.exceptions import AlgorithmRuntimeError
import random
import sys

value_range = range(10**8, 10**9)


def evaluate(algorithm):
    goals = {}
    goals["linear"] = (
        all(
            evaluate_case(algorithm, n, time_limit=0.1, also_absent=True)
            for n in (10, 100, 1000)
        )
    )
    goals["sublinear"] = (
        goals["linear"]
        and
        evaluate_case(algorithm, 1000000, time_limit=0.01, also_absent=True)
    )

    return {"goals": goals}


def evaluate_case(algorithm, n, time_limit, also_absent):
    vals = random.choices(value_range, k=n)
    val = random.choice(vals)
    try:
        index = run(algorithm, vals, val, time_limit)
    except AlgorithmRuntimeError as e:
        print(n, time_limit, e, file=sys.stderr)
        return False
    if vals[index] != val:
        return False;
    if also_absent:
        val = vals[0]
        while val in vals:
           val = random.choice(value_range)
        try:
            index = run(algorithm, vals, val, time_limit)
        except AlgorithmRuntimeError as e:
            print(n, time_limit, e, file=sys.stderr)
            return False
        if index != -1:
            return False
    return True


def run(algorithm, vals, val, time_limit):
    with algorithm.run() as process:
        process.call.store_list(len(vals), vals)
        with process.section(time_limit=time_limit):
            return process.call.find_val(val)
