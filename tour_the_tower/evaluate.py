from turingarena import *

algorithm = submitted_algorithm()

MAXN = 5


goals = {
    "correct_num_configs": True,
    "correct_move_tower": True,
}
for N in range(MAXN+1):
    def correct_num_valid_configurations(N):
        assert N >= 0
        return 3**N
    
    wrong_move = False
    rod = [1 for _ in range(N+1)] # stores a config: rod[disk] tells the peg on which disk is currently sitting. Disks are numbered from 1 to n.
    visited_conf = set()
    visited_conf.add(tuple(rod[1:(N+1)]))
    with algorithm.run() as process:
        # first, the minimum number of moves to move an N disks tower:
        risp = process.call.num_valid_configurations(N)
        if risp == correct_num_valid_configurations(N):
            print(f'num_valid_configurations({N:d}) -> {risp:d}. This is CORRECT.')
        else:
            print(f'num_valid_configurations({N:d}) -> {risp:d}. This is WRONG.')
            goals["correct_num_configs"] = False

        # and now let us move the tower:
        def move_disk(disk, peg_from, peg_to):
            print(f"Your solution commands to move disk {disk} from rod {peg_from} to rod {peg_to}.")
            if rod[disk] != peg_from:
                wrong_move = True
                print("The disk is not on the rod you told us to take it from!")
                exit()        
            if any(peg == peg_from  for peg in rod[1:disk]):
                wrong_move = True
                print("Can't move a disk which has a disk placed over it!")
                exit()        
            if any(peg == peg_to  for peg in rod[1:disk]):
                wrong_move = True
                print("Can't move a disk on top of a smaller one!")
                exit()        
            rod[disk] = peg_to
            if tuple(rod[1:(N+1)]) in visited_conf:
                wrong_move = True
                print("Configuration visited twice: {tuple(rod[1:(N+1)])}")
                exit()
                
            visited_conf.add(tuple(rod[1:(N+1)]))    

        process.call.visit_all_configs(N, move_disk=move_disk)
        if wrong_move:
            goals["correct_move_tower"] = False
        elif len(visited_conf) < correct_num_valid_configurations(N):
            goals["correct_move_tower"] = False
            print(f"Visited only {len(visited_conf)} configurations (done only {len(visited_conf)-1} moves). You are required to give a solution which visits each configuration precisely once!")
        else:
            print("Correct! You visited all configurations precisely once")
evaluation_result(goals=goals)
