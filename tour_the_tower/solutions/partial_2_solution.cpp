#include<cassert>

int num_valid_configurations(int n) {
  assert( n >= 0 );
  if( n==0 ) return 1;
  return 3*num_valid_configurations(n-1);
}

void move_disk(int disk, int from, int to);

void move_tower(int n, int from, int to, int aux) {
  assert( n >= 0 );
  if( n==0 ) return;
  move_tower(n-1, 0, 0, 0);
  move_disk(n, 0, 0);
  move_tower(n-1, 0, 0, 0);
}

void visit_all_configs(int n) {
  // starting form the valid configuration in which all <n> disks are orderly placed on rod 1, and moving one disk at the time, it makes the tower visit each valid configuration precisely once.
  move_tower(n, 1, 3, 2);
}
