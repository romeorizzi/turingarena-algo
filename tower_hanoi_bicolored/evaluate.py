from turingarena import *

import sys

algorithm = submitted_algorithm()

MAXN = 5






done_moves = 0
wrong_move = False
rod = [1 for _ in range(MAXN+2)]

goals = {
    "optimal_num_moves": True,
    "optimal_list_of_moves_without_pegs": True,
    "optimal_list_of_moves_with_pegs": True,
    "correct_list_of_moves_with_pegs": True,
}


for N in range(1, MAXN+1):
	# We define the correct number of moves needed
	# to complete the task.	
	def correct_num_moves(N):
		print(N)
		assert N >= 0
		if N==0:
			return 0
		elif N==1:
			return 3
		elif N==2:
			return 10
		else:
			return 11*(2**(N-1)-1)-3*(N-2)

	with algorithm.run() as process:
		risp = process.call.min_num_moves(N, 1, 3, 2)
		if risp == correct_num_moves(N):
			print(f'min_num_moves({N:d}) -> {risp:d}. This is CORRECT.', file=sys.stderr)
		else:
			print(f'min_num_moves({N:d}) -> {risp:d}. This is WRONG.', file=sys.stderr)
			goals["optimal_num_moves"] = False;
		
		done_moves = 0
		wrong_move = False

		rods = [
			None,
			[(i,0) for i in reversed(range(1, N+1))],
			[],
			[(i,1) for i in reversed(range(1, N+1))],
		]
		def move_disk(disk, peg_from, peg_to):
		    global done_moves, wrong_move, rod
		    print(f"Your solution ordered to move disk {disk} from rod {peg_from} to rod {peg_to}.", file=sys.stderr)
		    
		    assert len(rods[peg_from]) > 0
		    
		    actual_disk, actual_color = rods[peg_from].pop()
		    assert disk == actual_disk
		    
		    if len(rods[peg_to]) > 0:
		    	base_disk, base_color = rods[peg_to][-1]
		    	assert base_disk >= actual_disk
		    
		    rods[peg_to].append((actual_disk, actual_color))
		    
		    print("Rods:", file=sys.stderr)
		    for i in (1,2,3):
		    	print(f"Rod {i}:", *rods[i], file=sys.stderr)
		    
		    done_moves += 1

		process.call.bicolorProblem(N, 1, 3, 2, move_disk=move_disk)
		if wrong_move:
		    goals["correct_list_of_moves_with_pegs"] = False
		    goals["optimal_list_of_moves_without_pegs"] = False
		    goals["optimal_list_of_moves_with_pegs"] = False
		elif any(peg != 3  for peg in rod[1:]):
		    goals["correct_list_of_moves_with_pegs"] = False
		    goals["optimal_list_of_moves_without_pegs"] = False
		    goals["optimal_list_of_moves_with_pegs"] = False
		elif done_moves > correct_num_moves(N):
		    goals["optimal_list_of_moves_without_pegs"] = False
		    goals["optimal_list_of_moves_with_pegs"] = False
		    print(f"Tower of {N} disks moved in {done_moves} moves. Can be improved!", file=sys.stderr)
		else:
		    print(f"Tower of {N} disks moved in {done_moves} moves. This is optimal!", file=sys.stderr)
evaluation_result(goals=goals)
