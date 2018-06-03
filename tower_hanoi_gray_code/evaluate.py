from turingarena import *

algorithm = submitted_algorithm()

MAXN = 8

done_moves = 0
wrong_move = False
rod = [1 for _ in range(MAXN+2)] # stores a config: rod[disk] tells the peg on which disk is currently sitting. Disks are numbered from 1 to n.

goals = {
    "optimal_num_moves": True,
    "optimal_list_of_moves_without_pegs": True,
    "optimal_list_of_moves_with_pegs": True,
    "correct_list_of_moves_with_pegs": True,
}
for N in range(MAXN+1):
    def correct_num_moves(N):
        assert N >= 0
        if N==0:
            return 0
        return 2+3*correct_num_moves(N-1)
    
    with algorithm.run() as process:
        # first, the minimum number of moves to move an N disks tower:
        risp = process.call.num_moves(N)
        if risp == correct_num_moves(N):
            print(f'num_moves({N:d}) -> {risp:d}. This is CORRECT.')
        else:
            print(f'num_moves({N:d}) -> {risp:d}. This is WRONG.')
            goals["optimal_num_moves"] = False

        # and now let us move the tower:
        done_moves = 0
        wrong_move = False
        rod = [1 for _ in range(N+1)]
        def move_disk(disk, peg_from, peg_to):
            global done_moves, wrong_move, rod
            print(f"Your solution ordered to move disk {disk} from rod {peg_from} to rod {peg_to}.")
            if rod[disk] != peg_from:
                wrong_move = True
                print("The disk is not on the rod you told us to take it from!")
                exit()        
            if any(peg == peg_from  for peg in rod[1:disk]):
                wrong_move = True
                print("You moved a disk which had a disk placed over it!")
                exit()        
            if any(peg == peg_to  for peg in rod[1:disk]):
                wrong_move = True
                print("You are moving a disk on top of a smaller one!")
                exit()        
            rod[disk] = peg_to
            done_moves += 1

        process.call.tower_hanoi_gray_code(N, 1, 3, 2, move_disk=move_disk)
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
            print(f"Tower of {N} disks moved in {done_moves} moves. Can be improved!")
        else:
            print(f"Tower of {N} disks moved in {done_moves} moves. This is optimal!")
evaluation_result(goals=goals)
