// evaluation_assert data["goals"]["correct_num_configs"]
// evaluation_assert data["goals"]["correct_move_tower"]


#include<cassert>

int min_num_valid_configurations(int n) {
  assert( n >= 0 );
  if( n==0 ) return 1;
  return 3*min_num_valid_configurations(n-1);
}

void move_disk(int disk, int from, int to);

void move_tower(int n, int from, int to, int aux) {
  assert( n >= 0 );
  int num_valid_configurations = min_num_valid_configurations(n);
  for(int i = 1; i <= num_valid_configurations; i++) {
    int disk_to_be_moved = i & -i;
    switch (i%3) {
    case 1: move_disk(disk_to_be_moved, from, to);
      break;

    case 2: move_disk(disk_to_be_moved, from, aux);
      break;

    case 0: move_disk(disk_to_be_moved, aux, to);
      break;
    }
  }  
}

void visit_all_configs(int n) {
  // starting form the valid configuration in which all <n> disks are orderly placed on rod 1, and moving one disk at the time, it makes the tower visit each valid configuration precisely once.
  move_tower(n, 1, 3, 2);
}