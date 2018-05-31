#include <cstdio>
#include <cstdlib>
int area_of_polytope(int n, int** vertex);

int main() {
    int N;
    scanf("%d", &N);
    int **vertex;
    vertex = new int*[N];
    for(int i = 0; i < N; i++) {
        vertex[i] = new int[2];
        for(int j = 0; j < 2; j++) {
            scanf("%d", &vertex[i][j]);
        }
    }
    int risp;
    risp = area_of_polytope(N, vertex);
    printf("%d\n", risp);
}
