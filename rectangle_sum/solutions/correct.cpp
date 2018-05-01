// evaluation_assert data["goals"]["bilinear"]
// evaluation_assert data["goals"]["monolinear"]
// evaluation_assert data["goals"]["sublinear"]
#include<cassert>

const int MAXM = 5000;
const int MAXN = 5000;
int M,N;
int prefix_sum[MAXM+1][MAXN+1];
// prefix_sum[r][c] = \sum_{i=0}^{r-1} mat[i][j]

void get_matrix(int m, int n, int **mat) {
  M = m; N = n;
  for (int i=1; i<=M; i++)
    for (int j=1; j<=M; j++)
       prefix_sum[i][j] = mat[i-1][j-1]
	                   + prefix_sum[i-1][j]
	                   + prefix_sum[i][j+1]
	                   - prefix_sum[i-1][j-1];
}

int rectangle_sum(int r1, int r2, int c1, int c2) {
  assert( 0 <= r1 );
  assert( r1 <= r2 -1 );
  assert( r2 < M );
  assert( 0 <= c1 );
  assert( c1 <= c2 -1 );
  assert( c2 < N );
  return   prefix_sum[r2+1][c2+1]
         - prefix_sum[r2+1][c1  ];
         - prefix_sum[r1  ][c2+1];
         + prefix_sum[r1  ][r2  ];
}



