#include <cstdio>
#include <cstdlib>

int is_laminar_family(int n, int m, int *card, int **set_elem, void give_bad_pair_of_sets(int s1, int s2), void open_root_node(int s), void open_child_node(int s), void give_leaf_node(int elem), void close_node());

int main() {
    // checkpoint
    printf("%d\n", 0);
    // read n, m
    static int m;
    static int n;
    fflush(stdout);
    scanf("%d%d", &n, &m);
    // for s to m {...}
    static int *card;
    card = new int[m];
    for (int s = 0; s < m; s++) {
        // read card[s]
        fflush(stdout);
        scanf("%d", &card[s]);
    }
    // for s to m {...}
    static int **set_elem;
    set_elem = new int*[m];
    for (int s = 0; s < m; s++) {
        // for i to card[s] {...}
        set_elem[s] = new int[card[s]];
        for (int i = 0; i < card[s]; i++) {
            // read set_elem[s][i]
            fflush(stdout);
            scanf("%d", &set_elem[s][i]);
        }
    }
    // call res = is_laminar_family(n, m, card, set_elem) callbacks {...}
    static int res;
    res = is_laminar_family(n, m, card, set_elem, [](int s1, int s2) {
        // callback give_bad_pair_of_sets
        printf("%d %d\n", 1, 0);
        // write s1, s2
        printf("%d %d\n", s1, s2);
    }, [](int s) {
        // callback open_root_node
        printf("%d %d\n", 1, 1);
        // write s
        printf("%d\n", s);
    }, [](int s) {
        // callback open_child_node
        printf("%d %d\n", 1, 2);
        // write s
        printf("%d\n", s);
    }, [](int elem) {
        // callback give_leaf_node
        printf("%d %d\n", 1, 3);
        // write elem
        printf("%d\n", elem);
    }, []() {
        // callback close_node
        printf("%d %d\n", 1, 4);
    });
    // no more callbacks
    printf("%d %d\n", 0, 0);
    // write res
    printf("%d\n", res);
    // exit
    exit(0);
}
