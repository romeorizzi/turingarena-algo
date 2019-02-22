#include<cassert>

int min_num_moves(int n) {
  assert( n >= 0 );
  if( n==0 ) return 0;
  return 1 + 2*min_num_moves(n-1);
}

void move_disk(int disk, int from, int to);

void move_tower(int n, int from, int to, int aux) {
  // TO BE DONE
}
