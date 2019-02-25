/*
   generatore2
   a. costruisce un albero o foresta i cui nodi sono i set
   b. popola i nodi con gli elementi dell'universo
   Fino a qui la famiglia è laminare.
   Col seguente passo il problema era univoco:
   c. sceglie due nodi e tre elementi, e piazza un solo elemento in comune
      (i rimanenti due elementi, uno per nodo).
*/

#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#include <assert.h>

/* #define DEBUG */

#define  MaxN   10000
#define  MaxM   10000
#define  MaxH   10000

int N, M, H, seed;                 /* Numero di elementi, numero di set, altezza albero */
float p;                           /* Frazione dei nodi che diventano padri del livello successivo */

int set[MaxM+1];
int padre[MaxM+1];

int count[MaxN+1];
int elenco[MaxN+1][MaxH+2];


void init( int t );
void insert( int, int );
void delete( int, int );
int cmp(const void *x, const void *y);


int main(int argc, char *argv[]) {
  int i, j, k, r, t, ri, rj;
  int livello, first, last, end;

  if ( argc != 6 ||
       sscanf(argv[1], " %d", &N) != 1 ||
       sscanf(argv[2], " %d", &M) != 1 ||
       sscanf(argv[3], " %d", &H) != 1 ||
       sscanf(argv[4], " %d", &t) != 1 ||
       sscanf(argv[5], " %d", &seed) != 1 ){
    printf("generatore N M H p seed\n");
    return 1;
  }

  assert( 1 <= N && N <= MaxN );
  assert( 1 <= M && M <= MaxM );
  assert( 3 <= H && H <= MaxH );
  assert( 0 < t && t < 100 );    /*  p = t/100 */
  init( t );
  
  /* GENERAZIONE: CREA UN ALBERO DI SET */

  first = 0; /* nodi del primo livello */
  last = rand() % (M/H);
  for ( livello = 1; livello < H; livello++ ){
    if (livello < H-1 ){
      r = rand() % (M/H);
      end = last+1+r;
    } else {
      end = M-1;
    }

    /* i nodi nel livello corrente set[last+1..end] hanno il padre in set[first..first+t-1] */
    t = (int)(p * (float)(last-first)) + 1;
    for ( k = last+1; k <= end; k++ )
      padre[ k ] = first + (rand() % t);

    first = last+1;
    last = end;
  }
  
 /* GENERAZIONE: POPOLA GLI SET CON ELEMENTI */
  

  for ( j = 0; j < N; j++ ){
    i = j % M;
    while ( i != padre[ i ] ) {
      elenco[j][ count[j] ] = set[i];
      count[j]++;
      i = padre[ i ];
    } 
    elenco[j][ count[j] ] = set[i];
    count[j]++;
  }


  /* GENERAZIONE: CREA UNA BAD PAIR DI SETS */

  /* due set random distinti */
  ri = rand() % M;
  do {
    rj = rand() % M;
  } while ( rj == ri );

  /* tre elementi distinti */
  i = rand() % N;
  do {
    j = rand() % N;
    } while ( j == i );
  do {
    k = rand() % N;
  } while ( k == i || k == j );


  /* Condizione di bad pair 
     A[i][ri] = 1;   A[i][rj] = 0;    
     A[j][ri] = 0;   A[j][rj] = 1;    
     A[k][ri] = 1;   A[k][rj] = 1;    
  */
  insert( i, ri );
  delete( i, rj );
  delete( j, ri );
  insert( j, rj );
  insert( k, ri );
  insert( k, rj );

  /* ordina i set per ciascun elemento */
  for ( j = 0 ; j < N ; j++ )
    qsort( elenco[j], count[j], sizeof(int), cmp );

  /* STAMPA */
  
  printf( "%d %d\n", N, M);
  for ( j = 0 ; j < N ; j++ ){
    printf( "%d", count[j] );
    for ( i = 0; i < count[j]; i++ )
      printf( " %d", elenco[j][i]+1 );
    printf( "\n" );
  }

  return 0;
}

int cmp(const void *x, const void *y) {
  int *X = (int *) x;
  int *Y = (int *) y;

  return *X-*Y;
}

void init( int t ){
  int tmp, i, j;

  p = (float)t / (float)100;
  srand( seed );

  for ( i = 0 ; i < M ; i++ )
    set[i] = i;

  for ( i = 0 ; i < M ; i++ ) {
    j = rand() % (M - i) + i;
    tmp = set[i];
    set[i] = set[j];
    set[j] = tmp;
  }
  
  for ( i = 0 ; i < M ; i++ ) 
    padre[ i ] = i;

  for ( i = 0 ; i < N ; i++ ) 
    count[i] = 0;

}

void insert( int elemento, int set ){
  int i;

  for (i = 0; i < count[elemento]; i++)
    if (elenco[elemento][i] == set )
      return;
  elenco[elemento][ count[elemento] ] = set;
  count[elemento]++;
}

void delete( int elemento, int set ){
  int i;

  for (i = 0; i < count[elemento]; i++)
    if (elenco[elemento][i] == set ){
      elenco[elemento][i] = elenco[elemento][ count[elemento]-1 ];
      break;
    }
  count[elemento]--;
}

