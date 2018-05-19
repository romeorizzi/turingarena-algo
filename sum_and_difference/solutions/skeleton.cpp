#include <cstdio>
#include <cstdlib>
int biggest_of_two_different_naturals_with_given_sum_and_difference(int sum, int dif);

int main() {
    int sum, dif;
    scanf("%d%d", &sum, &dif);
    int answ;
    answ = biggest_of_two_different_naturals_with_given_sum_and_difference(sum, dif);
    printf("%d\n", answ);
}
