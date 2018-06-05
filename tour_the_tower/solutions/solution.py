# evaluation_assert data["goals"]["correct_num_configs"]
# evaluation_assert data["goals"]["correct_walk_tower"]
# evaluation_assert data["goals"]["correct_tour_tower"]


#include<cassert>

def num_valid_configurations(n):
  assert n >= 0
  if n==0:
      return 1
  return 3*num_valid_configurations(n-1)

# How to import: move_disk(disk, peg_from, peg_to) ???

def move_tower(n, peg_from, peg_to, peg_aux):
# moves a whole Hanoi tower of <n> disks from peg <peg_from> to peg <peg_to>.
# It does so through a sequence of moves that visits every valid configuration precisely once.
  assert n >= 0
  if n==0:
      return
  move_tower(n-1, peg_from, peg_to, peg_aux)
  move_disk(n, peg_from, peg_aux)
  move_tower(n-1, peg_to, peg_from, peg_aux)
  move_disk(n, peg_aux, peg_to)
  move_tower(n-1, peg_from, peg_to, peg_aux)

def visit_all_configs(n):
# starting form the valid configuration in which all <n> disks are orderly placed on rod 1, and moving one disk at the time, it makes the tower visit each valid configuration precisely once.
  move_tower(n, 1, 3, 2)

