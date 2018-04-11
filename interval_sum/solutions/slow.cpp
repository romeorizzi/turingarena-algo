// evaluation_assert data["goals"]["linear"]
// evaluation_assert not data["goals"]["sublinear"]
#include<cassert>

const int MAXN = 1000000;
int N;
int val[MAXN];

void get_sequence(int n, int *s) {
   N = n;
   for (int i=0; i<N; i++) {
     val[i] = s[i];
   }  
}

int interval_sum(int a, int b) {
  assert( 0 <= a );
  assert( a <= b -1 );
  assert( b < N );
  int risp = 0;
  for (int i=a; i<=b; i++)
     risp += val[i];

  return risp;
}

