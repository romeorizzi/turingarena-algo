import random
import sys
import turingarena as ta

value_range = range(10, 99)

goals={"correct":True,"linear_prepare":True,"sublinear_query":True}

def evaluate_case(n, a, b, time_limit_answer, time_limit_prepare):
    vals = [random.choice(value_range) for _ in range(n)]
    with ta.run_algorithm(ta.submission.source)  as process:
        try:
            with process.section(time_limit=time_limit_prepare):
                process.procedures.get_sequence(len(vals), vals)
        except ta.TimeLimitExceeded:
            goals["linear_prepare"] = False
            print ("You take too much time to get in the array and prepare for the queries to follow.")
            return
        except AlgorithmError as e:
            print("Error: ", e)
        try:
            with process.section(time_limit=time_limit_answer):
                risp = process.functions.interval_sum(a, b)
        except ta.TimeLimitExceeded:
            goals["sublinear_query"] = False
            print ("You take too much time to answer a query.")
        except ta.AlgorithmError as e:
            print("Error: ", e)
    if risp != sum(vals[a:b+1]):
        goals["correct"] = False
        goals["linear_prepare"] = False
        goals["sublinear_query"] = False
        print ("The sum value returned is not correct. On the query ({a},{b}) you return {risp} instead of {sum(vals[a:b+1])}.\nHere the array was {vals}")


for n in (10, 100, 1000):
    if goals["correct"] == True:
        evaluate_case(n, a=n//4, b=3*n//4, time_limit_answer=0.2, time_limit_prepare=0.2)
    if goals["linear_prepare"] == True:
        evaluate_case(n, a=n//4, b=3*n//4, time_limit_answer=0.2, time_limit_prepare=0.01)
    if goals["sublinear_query"] == True:
       evaluate_case(n, a=n//4, b=3*n//4, time_limit_answer=0.001, time_limit_prepare=0.2)
print(goals)

ta.goals["correct"] = goals["correct"]
ta.goals["linear_prepare"] = goals["linear_prepare"]
ta.goals["sublinear_query"] = goals["sublinear_query"]

