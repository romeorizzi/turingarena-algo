#include <cstdio>
#include <cstdlib>
int find_max(int n, int maxLies);
int compare(int a, int b) {
    printf("%d\n", 1);
    printf("%d\n", 0);
    printf("%d %d\n", a, b);
    fflush(stdout);
    int answ;
    scanf("%d", &answ);
    return answ;
}

int main() {
    int n, maxLies;
    scanf("%d%d", &n, &maxLies);
    int answ;
    answ = find_max(n, maxLies);
    printf("%d\n", 0);
    printf("%d\n", answ);
}
