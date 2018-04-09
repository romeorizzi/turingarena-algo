// evaluation_assert data["goals"]["linear"]
// evaluation_assert not data["goals"]["sublinear"]
#include <cassert>
#include <vector>

using std::vector;

const int NONE = -1;

int N;
vector<int> vals;

void store_list(int n, int *lista_vals) {
    vals.resize(n);
    for(int i = 0; i < n; i++)
        vals[i] = lista_vals[i];
}

int find_val(int val) {
    for(int i = 0; i < vals.size(); i++) {
        if(vals[i] == val) {
            return i;
        }
    }
    return NONE; 
}
