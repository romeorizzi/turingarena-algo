#include"assert.h"

int lsp(int n) {
  return n & (-n);
}

int is_power_of_2(int n) {
  return n == lsp(n);
}

int num_mosse_for_powers_of_two(int n) {
  assert(is_power_of_2(n));
  return 2*n-1;
}

int num_of_ones_in_binary_rep(int n) {
  if(n == 0)
    return 0;
  return 1 + num_of_ones_in_binary_rep(n - lsp(n));
}

int num_mosse(int n) {
  if(n==0)
    return 0;
  if(num_of_ones_in_binary_rep(n) % 2 == 1)
  //since the correct first move is move 1 (flip the rightmost bit), then:
    if(n%2 == 1)
      return 1 + num_mosse(n -1);
    else
      return 1 + num_mosse(n +1);
  if(lsp(n-lsp(n)) == 2*lsp(n))
    return 1 + num_mosse(n - 2*lsp(n));
  else
    return 1 + num_mosse(n + 2*lsp(n));
}

int mossa(int n) {
  assert(n > 0);
  if(num_of_ones_in_binary_rep(n) % 2 == 1)
    return 1;
  else
    return 2;
}

/*
#    n | num_mosse
#    1 |  1
#   10 |  3 = 1 + 1 + 1
#  100 |  7 = 3 + 1 + 3
# 1000 | 15 = 7 + 1 + 7 
*/
