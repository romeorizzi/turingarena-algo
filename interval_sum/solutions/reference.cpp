#include<cassert>

const int MAXN = 100000;
int N;

int _prefix_sum[MAXN+1];
int *prefix_sum = _prefix_sum +1;

void get_sequence(int n, int *s) {
   N = n;
   for (int i=0; i<N; i++)
     prefix_sum[i] = prefix_sum[i-1] + s[i];
}

int interval_sum(int a, int b) {
  assert( a >= 0 );
  assert( b >= a -1 );
  assert( b < N );
  return prefix_sum[b] - prefix_sum[a-1];
}



