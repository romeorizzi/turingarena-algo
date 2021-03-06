#include<cassert>

const int MAXM = 1000;
const int MAXN = 1000;
int M, N;
int val[MAXM][MAXN];

void get_matrix(int m, int n, int **mat) {
  assert( m <= MAXM );
  assert( n <= MAXN );
  M = m; N = n;
  for (int i=0; i<M; i++)
    for (int j=0; j<N; j++)
       val[i][j] = mat[i][j];
}

int rectangle_sum(int r1, int r2, int c1, int c2) {
  assert( 0 <= r1 );
  assert( r1 <= r2 );
  assert( r2 < M );
  assert( 0 <= c1 );
  assert( c1 <= c2 );
  assert( c2 < N );
  int risp = 0;
  for (int i=r1; i<=r2; i++)
     for (int j=c1; j<=c2; j++)
        risp += val[i][j];

  return risp;
}

