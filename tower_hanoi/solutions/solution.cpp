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
  move_tower(n-1, from, aux, to);
  move_disk(n, from, to);
  move_tower(n-1, aux, to, from);
}
