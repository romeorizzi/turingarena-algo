import random

NONE = -1

def compute(algorithm, a):
    with algorithm.run() as process:
        return process.call.repeated_val(len(a), a)


def evaluate(algorithm):
    for i in [1, 5, 10]:
        a = random.sample(range(10**9), i*10**4)
        dup_value = random.choice(a) 
        a.append(dup_value)
        random.shuffle(a)
        risp = compute(algorithm, a)

        if risp == dup_value:
            print("correct!")
        else:
            print("WRONG!")

        a = random.sample(range(10**9), i*10**4)
        random.shuffle(a)
        risp = compute(algorithm, a)

        if risp == NONE:
            print("correct!")
        else:
            print("WRONG!")

