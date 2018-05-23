#include <cstdio>
#include <cstdlib>
extern int nColors;
int blackScore(int c1, int c2, int c3, int c4) {
    printf("%d\n", 1);
    printf("%d\n", 0);
    printf("%d %d %d %d\n", c1, c2, c3, c4);
    fflush(stdout);
    int ans;
    scanf("%d", &ans);
    return ans;
}
int whiteScore(int c1, int c2, int c3, int c4) {
    printf("%d\n", 1);
    printf("%d\n", 1);
    printf("%d %d %d %d\n", c1, c2, c3, c4);
    fflush(stdout);
    int ans;
    scanf("%d", &ans);
    return ans;
}
void impossible() {
    printf("%d\n", 1);
    printf("%d\n", 2);
    exit(0);
}
void play();

__attribute__((constructor)) static void init() {
    scanf("%d", &nColors);
}

int main() {
    play();
    printf("%d\n", 0);
}
