#include<cassert>

const int MAXN = 100000;
int N;
int val[MAXN];
int **memo_risp;

void get_sequence(int n, int *s) {
   N = n;
   for (int i=0; i<N; i++) {
     val[i] = s[i];
   }
   memo_risp = new int*[N];
   for(int i=0; i<N; i++)
     memo_risp[i] = new int[N];
   for (int i=0; i<N; i++) {
       memo_risp[i][i] = s[i];
     for (int j=i+1; j<N; j++) {
       memo_risp[i][j] = memo_risp[i][j-1]+s[j];
     }
   }  
}

int interval_sum(int a, int b) {
  assert( a >= 0 );
  assert( b >= a -1 );
  assert( b < N );
  if(b<a)
    return 0;
  return memo_risp[a][b];
}

