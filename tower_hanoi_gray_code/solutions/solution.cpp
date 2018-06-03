// evaluation_assert data["goals"]["optimal_num_moves"]
// evaluation_assert data["goals"]["optimal_list_of_moves_without_pegs"]
// evaluation_assert data["goals"]["optimal_list_of_moves_with_pegs"]
// evaluation_assert data["goals"]["correct_list_of_moves_with_pegs"]


#include<cassert>

int num_moves(int n) {
  assert( n >= 0 );
  if( n==0 ) return 0;
  return 2 + 3*num_moves(n-1);
}

void move_disk(int disk, int from, int to);

void move_tower_hanoi_in_gray_code(int n, int from, int to, int aux) {
  assert( n >= 0 );
  if( n==0 ) return;
  move_tower_hanoi_in_gray_code(n-1, from, to, aux);
  move_disk(n, from, aux);
  move_tower_hanoi_in_gray_code(n-1, to, from, aux);
  move_disk(n, aux, to);
  move_tower_hanoi_in_gray_code(n-1, from, to, aux);
}
