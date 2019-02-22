from turingarena import *
import random

algorithm = submitted_algorithm()

goals = {
    "lcm2gcd_legal": True,   # it would be illegal to call oracle_lcm from lcm.
    "gcd2lcm_legal": True,   # it would be illegal to call oracle_gcd from gcd.
    "lcm2gcd_correct_always": True,
    "gcd2lcm_correct_for_positive_a_and_b": True,
    "gcd2lcm_correct_always": True
}

class UndueCallToOracle(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def oracle_gcd(a, b): # returns the greatest common divisor
#   gcd(a, b) is defined only for (a, b) >= (0, 0)
    global keep_count
    if keep_count:
        global num_calls_to_oracle_gcd
        num_calls_to_oracle_gcd += 1
    if a < 0 or b < 0:
        print(f"Your solution has called oracle_gcd({a},{b}). Notice that the greatest common divisor of a and b is defined only for (a, b) >= (0, 0).")
        return -1; # se la soluzione dello studente salta turingarena comunque dovrebbe rimanere in piedi!
    while a != b and a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a > 0:
        return a
    else:
        return b

#num_calls_to_oracle_oracle_lcm = 0
def oracle_lcm(a, b): # returns the least common multiple of a and b
#   lcm(a, b) is defined only for (a, b) >= (0, 0), plus also for (a, b) = (0, 0) with lcm(0, 0) = 0
    global keep_count
    if keep_count:
        global num_calls_to_oracle_lcm
        num_calls_to_oracle_lcm += 1

    if a < 0 or b < 0 or (a*b == 0 and a+b > 0):
        print(f"Your solution has called oracle_lcm({a},{b}). Notice that the least common multiple of a and b is defined only for (a, b) > (0, 0), plus also for (a, b) = (0, 0) with lcm(0, 0) = 0.")
        return -1; # se la soluzione dello studente salta turingarena comunque dovrebbe rimanere in piedi!

    keep_count_ = keep_count
    keep_count = False
    risp = 0
    if a > 0:    
        risp = (a*b)/oracle_gcd(a, b)
    keep_count = keep_count_
    return risp


for a in [random.randint(2, 10000) for _ in range(2)] + [1, 0]:
    for b in [random.randint(2, 10000) for _ in range(2)] + [1, 0]:
        with algorithm.run() as process:
            a_ = a
            b_ = b
            if a*b == 0:
                a_ = 0
                b_ = 0
            try:    
                num_calls_to_oracle_gcd = 0    
                num_calls_to_oracle_lcm = 0
                keep_count = True
                risp = process.call.lcm(a_,b_, oracle_gcd=oracle_gcd)
                keep_count = False
            except ValueError:
#            if num_calls_to_oracle_lcm > 0: 
                goals["reduce_lcm_to_gcd"] = False
                goals["lcm2gcd_legal"] = False
                print('You are not allowed to call the function oracle_lcm from within your function lcm. In computing lcm(a,b), you are allowed to call oracle_lcm. You should exploit this availability instead.')
                
            if num_calls_to_oracle_gcd == 0: 
                if a_*b_ > 0:
                    goals["lcm2gcd_correct_always"] = False
                    goals["lcm2gcd_correct_for_positive_a_and_b"] = False
                    print('EXPLANATION: The point of this exercise is not you to compute lcm(a, b) all by yourself. In computing lcm(a,b), you are allowed to call oracle_lcm. You should exploit the availability of this oracle! In this way, you will prove that the problem of computing lcm reduces to the problem of computing the gcd(a, b).')
            elif risp == oracle_lcm(a_,b_):
                print(f'lcm({a_},{b_}) -> {risp}. This is CORRECT.')
            else:
                print(f'lcm({a_},{b_}) -> {risp}. This is WRONG. The answer should be {oracle_lcm(a_,b_)}.')
                goals["lcm2gcd_correct_always"] = False
                    
            try:
                num_calls_to_oracle_gcd = 0    
                num_calls_to_oracle_lcm = 0    
                keep_count = True
                risp = process.call.gcd(a,b, oracle_lcm=oracle_lcm)
                keep_count = False
            except ValueError:
#            if num_calls_to_oracle_gcd > 0:
                print('You are not allowed to call the function oracle_gcd from within your function gcd. In computing gcd(a,b), you are allowed to call oracle_lcm. You should exploit this availability instead.')
                goals["gcd2lcm_legal"] = False
                goals["gcd2lcm_correct_always"] = False
                if a_*b_ > 0:
                    goals["gcd2lcm_correct_for_positive_a_and_b"] = False
                
            if num_calls_to_oracle_lcm == 0:
                if a_*b_ > 0:
                    goals["gcd2lcm_correct_always"] = False
                    goals["gcd2lcm_correct_for_positive_a_and_b"] = False
                    print('EXPLANATION: The point of this exercise is not you to compute gcd(a, b) all by yourself. In computing gcd(a,b), you are allowed to call oracle_lcm. You should exploit the availability of this oracle! In this way, you will prove that the problem of computing gcd can be reduced to the problem of computing the lcm(a, b), to which it is equivalent.')
            elif risp == oracle_gcd(a,b):
                print(f'gcd({a},{b}) -> {risp}. This is CORRECT.')
            else:
                print(f'gcd({a},{b}) -> {risp}. This is WRONG. The answer should be {oracle_gcd(a,b)}.')
                goals["gcd2lcm_correct_always"] = False
                if a_*b_ > 0:
                    goals["gcd2lcm_correct_for_positive_a_and_b"] = False

            

evaluation_result(goals=goals)
