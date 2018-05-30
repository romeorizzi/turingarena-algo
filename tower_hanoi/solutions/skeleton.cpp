#include <cstdio>
#include <cstdlib>
int min_num_moves(int n);
void move_disk(int disk, int from, int to) {
    printf("%d\n", 1);
    printf("%d\n", 0);
    printf("%d %d %d\n", disk, from, to);
    fflush(stdout);
}
void move_tower(int n, int from, int to, int aux);

int main() {
    int n;
    scanf("%d", &n);
    int ans;
    ans = min_num_moves(n);
    printf("%d\n", 0);
    printf("%d\n", ans);
    move_tower(n, 1, 3, 2);
    printf("%d\n", 0);
}
