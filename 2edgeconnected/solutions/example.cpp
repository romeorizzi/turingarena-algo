void build(int n, int *d, int **a, void start_component(), void add_node(int u), void add_bridge(int x, int y)) {
    start_component();
    add_node(0);

    start_component();
    add_node(1);

    add_bridge(0, 1);
}
