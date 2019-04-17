#include<cassert>

const int MAXN = 100000;
int N;
int val[MAXN];

void get_sequence(int n, int *s) {
   N = n;
   for (int i=0; i<N; i++) {
     val[i] = s[i];
   }  
}

int interval_sum(int a, int b) {
  assert( a >= 0 );
  assert( b >= a -1 );
  assert( b < N );
  int risp = 0;
  for (int i=a; i<=b; i++)
     risp += val[i];

  return risp;
}

