from turingarena import *

algorithm = submitted_algorithm()

done_moves = 0
wrong_move = False
rod = [1 for _ in range(10)] # stores a config: rod[disk] tells the peg on which disk is currently sitting

goals = {
    "optimal_num_moves": True,
}
for N in range(5):
    def correct_num_moves(N):
        assert N >= 0
        if N==0:
            return 0
        return 1+2*correct_num_moves(N-1)
    
    with algorithm.run() as process:
        risp = process.call.min_num_moves(N)
        if risp == correct_num_moves(N):
            print(f'min_num_moves({N:d}) -> {risp:d}. This is CORRECT.')
        else:
            print(f'min_num_moves({N:d}) -> {risp:d}. This is WRONG.')
            goals["optimal_num_moves"] = False
evaluation_result(goals=goals)
