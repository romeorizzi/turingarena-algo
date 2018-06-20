const int MAXN=100;
int father[MAXN];
int* TREE;
int cont=0;

void process(){
    int nodo=cont;
    int num_figli=TREE[cont];
    cont++;
    for(int i=0; i<num_figli; i++){
        father[cont]=nodo;
        process();
    }
}

void input_tree(int n, int *tree) {
    TREE=tree;
    process();
}

int father_of(int child) {
    return father[child];
}
