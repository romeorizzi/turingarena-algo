import random

from turingarena import *

algorithm = submitted_algorithm()

goals = {
    "correct_yes_no": True,
    "correct_with_certificate": True,
    "single_check_per_text_element": True,
}

MAX_VAL = 9

for len_t in [0, 1, 2, 10, 50]:
    text = [ random.randint(0, MAX_VAL) for _ in range(len_t) ]
    for len_p in [0, 1, 2, 10, 20]:
        if len_p <= len_t:
            arr = [1] * len_p + [0] * (len_t-len_p)
            random.shuffle(arr)
            pattern = [ text [i] for i in range(len_t) if arr[i] == 1 ]
        else:
            pattern = text + [ random.randint(0, MAX_VAL) for _ in range(len_p - len_t) ]
        if len_p <= len_t:
            p_subsequence_of_t = 1
        else:    
            p_subsequence_of_t = 0

        if len_p == 0 and len_t == 50:
            pattern = [ 5, 7, 2, 6, 9, 8]
            text = [ 3, 5, 7, 9, 2, 4, 6, 5, 8]
            len_p = len(pattern)
            len_t = len(text)
            p_subsequence_of_t = 0
            
        compared = [0] * len_t
        underlined = [0] * len_t

        def check(pos_p, pos_t):
            if not 1 <= pos_p <= len_p:
                print(f"Index not valid: pos_p = {pos_p}.")
            if not 1 <= pos_t <= len_t:
                print(f"Index not valid: pos_t = {pos_t}.")
            compared[pos_t-1] += 1
            if compared[pos_t-1] > 1:
                print(f"The element of index {pos_t} in the text has been compared {compared[pos_t-1]} times.")
                goals["single_check_per_text_element"] = False
            if text[pos_t-1] == pattern[pos_p-1]:
                return 1;
            return 0;

        def underline(pos_t):
            if not 1 <= pos_t <= len_t:
                print(f"Index not valid: pos_t = {pos_t}.")
            if underlined[pos_t-1] == 1:
                print("WARNING: you underlined twice or more a same element of the text")
            underlined[pos_t-1] = 1   

        
        with algorithm.run() as process:
            risp = process.call.subsequence(len_p, len_t, check=check, underline=underline)
            if p_subsequence_of_t:
                print("The pattern occurred as a subsequence in the text.")
            else:
                print("The pattern did NOT occurred as a subsequence in the text.")
            if risp == p_subsequence_of_t:
                print("Your solution got this right. This is CORRECT.")
            else:    
                print("Your solution said the contrary. This is WRONG.")
                goals["correct_yes_no"] = False
                
            if p_subsequence_of_t:
                if pattern == [ text [i] for i in range(len_t) if underlined[i] == 1 ]:
                   print("You correctly delivered a subsequence equal to the pattern.")
                else:
                    print("The underlined elements do non form a subsequence equal to the pattern.")
                    goals["correct_with_certificate"] = False


evaluation_result(goals=goals)
