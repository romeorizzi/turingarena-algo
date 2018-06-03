# evaluation_assert data["goals"]["optimal_num_moves"]
# evaluation_assert data["goals"]["optimal_list_of_moves_without_pegs"]
# evaluation_assert data["goals"]["optimal_list_of_moves_with_pegs"]
# evaluation_assert data["goals"]["correct_list_of_moves_with_pegs"]


#include<cassert>

def num_moves(n):
  assert n >= 0
  if n==0:
      return 0
  return 2 + 3*num_moves(n-1)

# How to import: move_disk(disk, peg_from, peg_to) ???

def move_tower_hanoi_in_gray_code(n, peg_from, peg_to, peg_aux):
  assert n >= 0
  if n==0:
      return
  move_tower_hanoi_in_gray_code(n-1, peg_from, peg_to, peg_aux)
  move_disk(n, peg_from, peg_aux)
  move_tower_hanoi_in_gray_code(n-1, peg_to, peg_from, peg_aux)
  move_disk(n, peg_aux, peg_to)
  move_tower_hanoi_in_gray_code(n-1, peg_from, peg_to, peg_aux)

