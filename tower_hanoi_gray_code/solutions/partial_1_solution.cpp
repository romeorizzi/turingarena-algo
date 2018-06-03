// evaluation_assert data["goals"]["optimal_num_moves"]
// evaluation_assert not data["goals"]["optimal_list_of_moves_without_pegs"]
// evaluation_assert not data["goals"]["optimal_list_of_moves_with_pegs"]
// evaluation_assert not data["goals"]["correct_list_of_moves_with_pegs"]


#include<cassert>

int num_moves(int n) {
  assert( n >= 0 );
  if( n==0 ) return 0;
  return 2 + 3*num_moves(n-1);
}

void move_disk(int disk, int from, int to);

void move_tower_hanoi_in_gray_code(int n, int from, int to, int aux) {
  // TO BE DONE
}
