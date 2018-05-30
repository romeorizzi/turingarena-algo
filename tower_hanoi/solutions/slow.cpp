// evaluation_assert data["goals"]["optimal_num_moves"]
// evaluation_assert data["goals"]["optimal_list_of_moves_without_pegs"]
// evaluation_assert data["goals"]["optimal_list_of_moves_with_pegs"]
// evaluation_assert data["goals"]["correct_list_of_moves_with_pegs"]


#include<cassert>

int min_num_moves(int n) {
  assert( n >= 0 );
  if( n==0 ) return 0;
  return min_num_moves(n-1) +1 +min_num_moves(n-1);
}

void move_disk(int disk, int from, int to);

void move_tower(int n, int from, int to, int aux) {
  assert( n >= 0 );
  if( n==0 ) return;
  move_tower(n-1, from, aux, to);
  move_disk(n, from, to);
  move_tower(n-1, aux, to, from);
}
