import random
import sys
import turingarena as ta

value_range = range(10, 99)

goals={"correct":True,"constant_query":True,"linear_storage":True,"linear_storage_time":True}

def evaluate_case(n, a, b, time_limit_answer, storage_memory_limit, storage_time_limit):
    vals = [random.choice(value_range) for _ in range(n)]
    with ta.run_algorithm(ta.submission.source)  as p:
        try:
            with p.section(memory_limit=100*storage_memory_limit,time_limit=100*storage_time_limit) as s:
                p.procedures.get_sequence(len(vals), vals)
            time_usage = s.time_usage
            print(f"(get_sequence time_usage={time_usage} us)")
        except ta.MemoryLimitExceeded:
            goals["linear_storage"] = False
            print ("You use too much memory.")
            return
        except ta.TimeLimitExceeded:
            goals["linear_storage_time"] = False
            print ("Your procedure get_sequence takes far too much time.")
            return
 #       except ta.AlgorithmRuntimeError, ta.AlgorithmError as e:
        except ta.AlgorithmRuntimeError as e:
            print("Error: ", e)
            return
        if int(time_usage*1000000) > 1000:
            goals["linear_storage_time"] = False
            print ("Your procedure get_sequence takes too much time.")

        p.checkpoint()

        try:
            with p.section(time_limit=100*time_limit_answer) as s:
                risp = p.functions.interval_sum(a, b)
            time_usage = s.time_usage
            print(f"(interval_sum time: {s.time_usage} us)")
        except ta.TimeLimitExceeded:
            goals["constant_query"] = False
            print ("You take too much time to answer a query.")
            return
        except ta.AlgorithmError as e:
#        except ta.AlgorithmRuntimeError, ta.AlgorithmError as e:
            print("Error: ", e)
            return
        if int(time_usage*1000000) > 1000:
            goals["constant_query"] = False
            print ("Your procedure interval_sum takes too much time.")
    
    if risp != sum(vals[a:b+1]):
        goals["correct"] = False
        goals["constant_query"] = False
        goals["linear_storage"] = False
        goals["linear_storage_time"] = False
        print (f"The sum value returned is not correct. On the query ({a},{b}) you return {risp} instead of {sum(vals[a:b+1])}.\nHere the array was {vals}")


for n in (10, 100, 1000, 10000):
    if goals["correct"] == True:
        evaluate_case(n, a=n//4, b=3*n//4, time_limit_answer=0.2, storage_memory_limit=48*1024*1024, storage_time_limit=0.2)

    if goals["constant_query"] == True:
       evaluate_case(n, a=n//4, b=3*n//4, time_limit_answer=0.0005, storage_memory_limit=2048*1024*1024, storage_time_limit=0.2)
        
    if goals["linear_storage"] == True:
        evaluate_case(n, a=n//4, b=3*n//4, time_limit_answer=0.2, storage_memory_limit=32*1024*1024, storage_time_limit=0.2)

    if goals["linear_storage_time"] == True:
        evaluate_case(n, a=n//4, b=3*n//4, time_limit_answer=0.2, storage_memory_limit=2048*1024*1024, storage_time_limit=0.0005)

print(goals)

ta.goals["correct"] = goals["correct"]
ta.goals["constant_query"] = goals["constant_query"]
ta.goals["linear_storage"] = goals["linear_storage"]
ta.goals["linear_storage_time"] = goals["linear_storage_time"]
