#include<cassert>
#include <cstdio>
#include <cstdlib>

const int MAXM = 5000;
const int MAXN = 5000;
int M, N;
int prefix_sum[MAXM][MAXN+1];
// prefix_sum[r][0] = 0 
// prefix_sum[r][c] = \sum_{j=0}^{c-1} mat[r][j]

void get_matrix(int m, int n, int **mat) {
  assert( m <= MAXM );
  assert( n <= MAXN );
  M = m; N = n;
  for (int i=0; i<M; i++)
    for (int j=1; j<=N; j++)
       prefix_sum[i][j] = mat[i][j-1] + prefix_sum[i][j-1];
  /* fprintf(stderr, "Prefix sums of the rows:\n");
  for (int i=0; i<M; i++) {
    for (int j=0; j<=N; j++)
      fprintf(stderr, "%d ", prefix_sum[i][j]);
    fprintf(stderr, "\n");
    }  */
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
        risp += prefix_sum[i][c2+1] - prefix_sum[i][c1];
  return risp;
}

