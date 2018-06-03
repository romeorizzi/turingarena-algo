// evaluation_assert data["goals"]["optimal_num_moves"]
// evaluation_assert data["goals"]["optimal_list_of_moves_without_pegs"]
// evaluation_assert data["goals"]["optimal_list_of_moves_with_pegs"]
// evaluation_assert data["goals"]["correct_list_of_moves_with_pegs"]


#include<cassert>

int min_num_moves(int n) {
  assert( n >= 0 );
  if( n==0 ) return 0;
  return 1 + 2*min_num_moves(n-1);
}

void move_disk(int disk, int from, int to);

void move_tower(int n, int from, int to, int aux) {
  assert( n >= 0 );
  int num_moves = min_num_moves(n);
  for(int i = 1; i <= num_moves; i++) {
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

