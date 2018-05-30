from turingarena import *

algorithm = submitted_algorithm()

done_moves = 0
wrong_move = False
rod = [1 for _ in range(10)] # stores a config: rod[disk] tells the peg on which disk is currently sitting

goals = {
    "optimal_num_moves": True,
    "optimal_list_of_moves_without_pegs": True,
    "optimal_list_of_moves_with_pegs": True,
    "correct_list_of_moves_with_pegs": True,
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
        done_moves = 0
        wrong_move = False
        rod = [1 for _ in range(N)]
        def move_disk(disk, peg_from, peg_to):
            global done_moves, wrong_move, rod
            print(f"Your solution ordered to move disk {disk} from rod {peg_from} to rod {peg_to}.")
            if rod[disk] != peg_from:
                wrong_move = True # c
                print("The disk is not on the rod you told us to take it from!")
                exit()        
            if any(peg == peg_from  for peg in rod[0..disk]):
                wrong_move = True
                print("You moved a disk which had a disk placed over it!")
                exit()        
            if any(peg == peg_to  for peg in rod[0..disk]):
                wrong_move = True
                print("You are moving a disk on top of a smaller one!")
                exit()        
            rod[disk] = peg_to
            done_moves += 1

        process.call.move_tower(N, 1, 3, 2)
        if wrong_move:
            goals["correct_list_of_moves_with_pegs"] = False
            goals["optimal_list_of_moves_without_pegs"] = False
            goals["optimal_list_of_moves_with_pegs"] = False
        elif rod != [1 for _ in range(N)]:
            goals["correct_list_of_moves_with_pegs"] = False
            goals["optimal_list_of_moves_without_pegs"] = False
            goals["optimal_list_of_moves_with_pegs"] = False
        elif done_moves > num_moves(N):
            goals["optimal_list_of_moves_without_pegs"] = False
            goals["optimal_list_of_moves_with_pegs"] = False
            print(f"Tower of {N} disks moved in {done_moves} moves. Can be improved!")
        else:
            print(f"Tower of {N} disks moved in {done_moves} moves. This is optimal!")
evaluation_result(goals=goals)
