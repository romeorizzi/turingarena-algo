from turingarena.sandbox.exceptions import AlgorithmRuntimeError
import random
import sys

value_range = range(10**8, 10**9)


def evaluate(algorithm):
    goals = {}
    goals["linear"] = (
        all(
            evaluate_present(algorithm, n, time_limit=0.1)
            for n in (10, 100, 1000)
        )
        and
        all(
            evaluate_absent(algorithm, n, time_limit=0.1)
            for n in (10, 100, 1000)
        )
    )
    goals["sublinear"] = (
        goals["linear"]
        and
        evaluate_present(algorithm, 1000000, time_limit=0.01)
        and
        evaluate_absent(algorithm, 1000000, time_limit=0.01)
    )

    return {"goals": goals}


def evaluate_present(algorithm, n, time_limit):
    vals = random.choices(value_range, k=n)
    val = random.choice(vals)
    try:
        index = run(algorithm, vals, val, time_limit)
    except AlgorithmRuntimeError as e:
        print(n, time_limit, e, file=sys.stderr)
        return False
    return vals[index] == val


def evaluate_absent(algorithm, n, time_limit):
    vals = random.choices(value_range, k=n)
    val = vals[0]
    while val in vals:
        val = random.choice(value_range)
    try:
        index = run(algorithm, vals, val, time_limit)
    except AlgorithmRuntimeError as e:
        print(n, time_limit, e, file=sys.stderr)
        return False
    return index == -1


def run(algorithm, vals, val, time_limit):
    with algorithm.run() as process:
        process.call.store_list(len(vals), vals)
        with process.section(time_limit=time_limit):
            return process.call.find_val(val)
