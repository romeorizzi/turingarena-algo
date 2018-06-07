#include <cstdio>
#include <cstdlib>
void process_comparisons(int n, int* a, int* b);
void cycle(int v) {
    printf("%d\n", 1);
    printf("%d\n", 0);
    printf("%d\n", v);
}
void first_topological_sort(int v) {
    printf("%d\n", 1);
    printf("%d\n", 1);
    printf("%d\n", v);
}
void second_topological_sort(int v) {
    printf("%d\n", 1);
    printf("%d\n", 2);
    printf("%d\n", v);
}

int main() {
    int n;
    int *a;
    int *b;
    scanf("%d", &n);
    a = new int[n];
    b = new int[n];
    for(int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        scanf("%d", &b[i]);
    }
    process_comparisons(n, a, b);
    printf("%d\n", 0);
}
