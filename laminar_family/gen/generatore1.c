#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#include <assert.h>

/* #define DEBUG */

#define  MaxN   10000
#define  MaxM   10000


char A[MaxN+1][MaxM+1];   /* Matrice atleti x sponsor */
int N, M, L, legge, seed;                 /* Numero di atleti e numero di sponsor */

void init( ){
  int i,j;

  srand( seed );

  for ( i = 0 ; i < N ; i++ )
    for ( j = 0; j < M; j++ )
      A[i][j] = 0;
}


int main(int argc, char *argv[]) {
  int i, j, k, r, ri, rj, count;
  char soloj, solok, siajsiak;
  char leggeSoddisfatta;

  if ( argc != 6 ||
       sscanf(argv[1], " %d", &N) != 1 ||
       sscanf(argv[2], " %d", &M) != 1 ||
       sscanf(argv[3], " %d", &L) != 1 ||
       sscanf(argv[4], " %d", &legge) != 1 ||
       sscanf(argv[5], " %d", &seed) != 1 ){
    printf("generatore N M L [0|1] seed\n");
    return 1;
  }

  assert( 1 <= N && N <= MaxN );
  assert( 1 <= M && M <= MaxM );
  assert( 1 <= L && L <= MaxN * MaxM );
  assert( 0 <= legge && legge <= 1 );
  init( );
  
  /* GENERAZIONE: CREA UN ALBERO DI INSIEMI/COLONNE */
  
  for ( count = r = 0 ; r < L ; r++ ){
    ri = rand() % N;
    rj = rand() % M;
    A[ri][rj] = 1;
    
    /* Verifica se non rispetta il noto principio del marketing */
    leggeSoddisfatta = 1;
    j = rj;
    k = 0;
    while (leggeSoddisfatta && k < M) {
      soloj = 0;
      solok = 0;
      siajsiak = 0;
      for ( i = 0; i < N; i++ ){
	if (A[i][j] && !A[i][k]) soloj = 1;
	if (!A[i][j] && A[i][k]) solok = 1;
	if (A[i][j] && A[i][k]) siajsiak = 1;
      }
      if ( soloj && solok && siajsiak )
	leggeSoddisfatta = 0;
      else 
	k++;
    }

    if (!leggeSoddisfatta) 
      A[ri][rj] = 0; 
    else
      count++;
  }

  if (count != L )
    fprintf( stderr, "\ngenerati %d elementi su L=%d richiesti (parametri %d %d %d %d %d)\n", count, L, N, M, L, legge, seed );
  if (!legge){
    /* due colonne random distinte */
    ri = rand() % M;
    do {
      rj = rand() % M;
    } while ( rj == ri );

    /* tre righe random distinte */
    i = rand() % N;
    do {
      j = rand() % N;
    } while ( j == i );
    do {
      k = rand() % N;
    } while ( k == i || k == j );

    /* Condizione che viola il noto principio del marketing */
    A[i][ri] = 1;   A[i][rj] = 0;    
    A[j][ri] = 0;   A[j][rj] = 1;    
    A[k][ri] = 1;   A[k][rj] = 1;    
  }

#ifdef DEBUG
  for ( i = 0 ; i < N ; i++ ){
    printf("%d", A[i][0]);
    for (j=1; j < M; j++)
      printf(" %d", A[i][j]);
    printf("\n");
  }
  printf("\n");
#endif


  /* STAMPA */
  
  printf( "%d %d\n", N, M);
  for ( i = 0 ; i < N ; i++ ){
    for ( count = j = 0; j < M; j++ )
      if ( A[i][j] ) count++;
    printf( "%d", count );
    for ( j = 0; j < M; j++ )
      if ( A[i][j] ) printf( " %d", j+1 );
    printf( "\n" );
  }

  return 0;
}
