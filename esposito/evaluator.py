from turingarena import *

algorithm = submitted_algorithm()
tree = [3, 3, 0, 1, 0, 0, 2, 0, 2, 0, 0, 1, 0]
with algorithm.run() as process:
    process.procedures.input_tree(len(tree), tree)
    for i in range(13):
        ans = process.functions.father_of(i)
        print(ans )

