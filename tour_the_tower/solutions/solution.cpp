// evaluation_assert data["goals"]["correct_num_configs"]
// evaluation_assert data["goals"]["correct_walk_tower"]
// evaluation_assert data["goals"]["correct_tour_tower"]


#include<cassert>

int num_valid_configurations(int n) {
  assert( n >= 0 );
  if( n==0 ) return 1;
  return 3*num_valid_configurations(n-1);
}

void move_disk(int disk, int from, int to);

void move_tower(int n, int from, int to, int aux) {
// moves a whole Hanoi tower of <n> disks from peg <peg_from> to peg <peg_to>.
// It does so through a sequence of moves that visits every valid configuration precisely once.
  assert( n >= 0 );
  if( n==0 ) return;
  move_tower(n-1, from, to, aux);
  move_disk(n, from, aux);
  move_tower(n-1, to, from, aux);
  move_disk(n, aux, to);
  move_tower(n-1, from, to, aux);
}

void visit_all_configs(int n) {
  // starting form the valid configuration in which all <n> disks are orderly placed on rod 1, and moving one disk at the time, it makes the tower visit each valid configuration precisely once.
  move_tower(n, 1, 3, 2);
}
