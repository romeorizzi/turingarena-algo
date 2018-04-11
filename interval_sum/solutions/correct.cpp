// evaluation_assert data["goals"]["linear"]
// evaluation_assert data["goals"]["sublinear"]
#include<cassert>

const int MAXN = 1000000;
int N;
int _prefix_sum[MAXN+1];
int *prefix_sum = _prefix_sum +1;

void get_sequence(int n, int *s) {
   N = n;
   for (int i=0; i<N; i++)
     prefix_sum[i] = prefix_sum[i-1] + s[i];
}

int interval_sum(int a, int b) {
  assert( 0 <= a );
  assert( a <= b -1 );
  assert( b < N );
  return prefix_sum[b] - prefix_sum[a-1];
}



