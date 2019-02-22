#include <cstdio>
#include <cstdlib>
#include <cassert>

extern "C" {

int num_modi(int n);

void elenca_modi(int n, void pescato_intera(), void pescato_mezza(), void done());

} // extern "C"

int main() {
    // checkpoint
    printf("%d\n", 0);
    // read n
    static int n;
    fflush(stdout);
    scanf("%d", &n);
    // call res = num_modi(n)
    static int res;
    res = num_modi(n);
    // write res
    printf("%d\n", res);
    // read choice
    static int choice;
    fflush(stdout);
    scanf("%d", &choice);
    // if choice {...}
    if (choice) {
        // read n1
        static int n1;
        fflush(stdout);
        scanf("%d", &n1);
        // call elenca_modi(n1) callbacks {...}
        elenca_modi(n1, []() {
            // callback pescato_intera
            printf("%d %d\n", 1, 0);
        }, []() {
            // callback pescato_mezza
            printf("%d %d\n", 1, 1);
        }, []() {
            // callback done
            printf("%d %d\n", 1, 2);
        });
        // no more callbacks
        printf("%d %d\n", 0, 0);
    }
    // exit
    exit(0);
}
