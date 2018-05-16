#include <cstdio>
#include <cstdlib>
void get_matrix(int m, int n, int** mat);
int rectangle_sum(int r1, int r2, int c1, int c2);

int main() {
    int M, N;
    scanf("%d%d", &M, &N);
    int **mat;
    mat = new int*[M];
    for(int i = 0; i < M; i++) {
        mat[i] = new int[N];
        for(int j = 0; j < N; j++) {
            scanf("%d", &mat[i][j]);
        }
    }
    printf("I've got M= %d and N= %d\n",M,N);
    printf("I have read the following matrix:\n");
    for (int i=0; i<M; i++) {
       for (int j=0; j<N; j++)
         printf("%d ", mat[i][j]);
       printf("\n");
    }  

    get_matrix(M, N, mat);
    printf("%d\n", 0);
    fflush(stdout);
    int r1, r2, c1, c2, risp;
    do {
       scanf("%d%d%d%d", &r1, &r2, &c1, &c2);
       printf("r1=%d, r2=%d, c1=%d,  c2=%d --> ", r1, r2, c1, c2);
       risp = rectangle_sum(r1, r2, c1, c2);
       printf("%d\n", risp);
    } while (r1 <= r2);  
  
    return 0;
}
