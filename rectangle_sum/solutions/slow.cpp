// evaluation_assert data["goals"]["bilinear"]
// evaluation_assert data["goals"]["monolinear"]
// evaluation_assert not data["goals"]["sublinear"]
#include<cassert>

const int MAXM = 5000;
const int MAXN = 5000;
int M, N;
int val[MAXM][MAXN];
int prefix_sum[MAXM][MAXN+1];
// prefix_sum[r][c] = \sum_{j=0}^{c-1} mat[r][j]

void get_matrix(int m, int n, int **mat) {
  M = m; N = n;
  for (int i=0; i<M; i++)
    for (int j=1; j<=M; j++)
       prefix_sum[i][j] = mat[i][j] + prefix_sum[i][j-1];
}

int rectangle_sum(int r1, int r2, int c1, int c2) {
  assert( 0 <= r1 );
  assert( r1 <= r2 -1 );
  assert( r2 < M );
  assert( 0 <= c1 );
  assert( c1 <= c2 -1 );
  assert( c2 < N );
  int risp = 0;
  for (int i=r1; i<=r2; i++)
        risp += prefix_sum[i][r2+1] - prefix_sum[i][r1];
  return risp;
}

