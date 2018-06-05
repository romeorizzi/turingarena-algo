// evaluation_assert data["goals"]["correct_num_configs"]
// evaluation_assert not data["goals"]["correct_move_tower"]


#include<cassert>

int num_valid_configurations(int n) {
  assert( n >= 0 );
  if( n==0 ) return 1;
  return 3*num_valid_configurations(n-1);
}

void move_disk(int disk, int from, int to);

void visit_all_configs(int n) {
  // starting form the valid configuration in which all <n> disks are orderly placed on rod 1, and moving one disk at the time, it makes the tower visit each valid configuration precisely once.

  // TO BE DONE
}
