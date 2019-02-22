import random

from turingarena import *

algorithm = submitted_algorithm()

correct = True
correct_when_solution_exists = True
correct_when_integral = True
correct_when_different = True
correct_when_non_negative = True
correct_when_difference_non_negative = True

def main():
    for _ in range(10):
        value_range = range(10 ** 3, 5 * 10 ** 3)
        A, B = random.choices(value_range, k=2)
        sum_val, dif_val = A+B, A-B
        evaluate_case(algorithm, sum_val, dif_val)
    evaluate_case(algorithm, sum_val=4, dif_val=1) # only fractional solutions case
    evaluate_case(algorithm, sum_val=4, dif_val=0) # only solutions with equal numbers case
    evaluate_case(algorithm, sum_val=10, dif_val=14) # only solutions with one negative numbers case

    evaluation_result(goals=dict(correct=correct,correct_when_solution_exists=correct_when_solution_exists,correct_when_integral=correct_when_integral,correct_when_different=correct_when_different,correct_when_non_negative=correct_when_non_negative,correct_when_difference_non_negative=correct_when_difference_non_negative))

def solution_exists (sum_val, dif_val):
    if (sum_val%2) != (dif_val%2):
        print("no solution: they can't be integer")
        return False # they can't be integer
    if(sum_val < dif_val):
        print("no solution: they can't be both positive")
        return False # they can't be both positive    
    if(dif_val < 1):
        print("no solution: they can't be different")
        return False # they can't be different
    print("This instance admits a solution")
    return True
    
def evaluate_case(algorithm, sum_val, dif_val):
    try:
        with algorithm.run() as process:
            big = process.call.biggest_of_two_different_naturals_with_given_sum_and_difference(sum_val, dif_val)
        small = sum_val - big
        if solution_exists (sum_val, dif_val):
            if big == -1:
               correct = False
               correct_when_solution_exists = False
               correct_when_integral = False
               correct_when_different = False
               correct_when_non_negative = False
               correct_when_difference_non_negative = False
               print(f"Wrong: you wrongly asserted that no solution exists when sum={sum_val} and dif={dif_val}, but consider the pair:", (sum_val, - dif_val)/2, (sum_val, - dif_val)/2 -dif_val)
            if big != -1:
                if big-small != dif_val:
                    correct = False
                    correct_when_solution_exists = False
                    correct_when_integral = False
                    correct_when_different = False
                    correct_when_non_negative = False
                    correct_when_difference_non_negative = False
                    print("Wrong: the solution to problem sum=%d, dif=%d is: %d, %d and not %d, %d", (sum_val, dif_val, (sum_val - dif_val)/2, (sum_val - dif_val)/2 -dif_val))
                    print(f"Wrong: the solution to problem sum=%d{sum_val}, dif={dif_val} is:")
                    print ((sum_val - dif_val)/2, (sum_val - dif_val)/2 -dif_val)
                    print(f"and not {big} {small}")
                    
        if not solution_exists (sum_val, dif_val):
            if (big != -1):
                print(f"Wrong: you did not detect that the problem sum={sum_val}, dif={dif_val} admits no solution")
                correct = False
                if (sum_val%2) == (dif_val%2):
                    correct_when_integral = False
                if(sum_val > dif_val):
                    correct_when_non_negative = False
                if(dif_val > 0):
                    correct_when_different = False
                    correct_when_difference_non_negative = False
    except AlgorithmError as e:
        print(f"Eccezzione su chiamata sum={sum_val}, dif={dif_val}")
        all_passed = False

    return True

main()
