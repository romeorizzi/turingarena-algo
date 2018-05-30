// evaluation_assert data["goals"]["optimal_num_moves"]
// evaluation_assert data["goals"]["optimal_list_of_moves_without_pegs"]
// evaluation_assert not data["goals"]["optimal_list_of_moves_with_pegs"]
// evaluation_assert not data["goals"]["correct_list_of_moves_with_pegs"]


#include<cassert>

int min_num_moves(int n) {
  assert( n >= 0 );
  if( n==0 ) return 0;
  return 1 + 2*min_num_moves(n-1);
}

void move_disk(int disk, int from, int to);

void move_tower(int n, int from, int to, int aux) {
  assert( n >= 0 );
  if( n==0 ) return;
  move_tower(n-1, 0, 0, 0);
  move_disk(n, 0, 0);
  move_tower(n-1, 0, 0, 0);
}
