#include <cstdio>
#include <cstdlib>

void store_the_numbers(int n, int* val);
void orderly_list_the_pairs_of_numbers_with_sum(int SUM);
void deliver_pair(int small, int big) {
    printf("%d\n", 1);
    printf("%d\n", 0);
    printf("%d %d\n", small, big);
    fflush(stdout);
}

int main() {
    int N;
    scanf("%d", &N);
    int *vec;
    vec = new int[N];
    for(int i = 0; i < N; i++) {
        scanf("%d", &vec[i]);
    }
    store_the_numbers(N, vec);
    printf("%d\n", 0);
    int SUM;
    scanf("%d", &SUM);
    printf("%d\n", 0);
    fflush(stdout);
    orderly_list_the_pairs_of_numbers_with_sum(SUM);
    printf("%d\n", 0);
}
