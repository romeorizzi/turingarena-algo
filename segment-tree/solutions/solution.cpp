#include<cassert>
#include<iostream>

using namespace std;

const int MAXN = (1<<20) +1;
int n, vec[MAXN+1];

struct node {
  int sum;
};

node tree[MAXN+1];
  
void segmentation_tree_init(const int id, const int first, const int last) {
    assert(first <= last);
    cout << "id node = " <<  id << ", first = " <<  first << ", last = " << last << endl; 
    if(first == last) // We are in a leaf id, responsible of one single element
        tree[id].sum = vec[first];
    else {
        int mid = (first + last) / 2;
        segmentation_tree_init(2*id, first, mid);   // Recurse on the left child
        segmentation_tree_init(2*id+1, mid+1, last);  // Recurse on right child
        tree[id].sum = tree[2*id].sum + tree[2*id+1].sum;
    }
}

int get_sum(const int id, const int first, const int last, const int fq, const int lq) {
/* dear node id of the segmentation tree,
      you that are responsible of the [first,last] subinterval of the segmentation tree,
   please, answer the query with query interval [fq,lq), for what portion of it falls within your competence.
*/   
    assert(first <= last);
    cout << "id node = " <<  id << ", first = " <<  first << ", last = " << last  << ", fq = " <<  fq << ", lq = " << lq << endl; 
  if (last < fq || first > lq) // fully outside. Nothing to do!
    return 0;

  if (fq <= first && last <= lq) // fully inside. Node id holds the final answer
    return tree[id].sum;

  //else
  int mid = (last + first) / 2;

  return get_sum(2 * id, first, mid, fq, lq) +
         get_sum(2 * id + 1, mid, last, fq, lq);
}

void update_element(int id, int first, int last, int pos, int add_val) {
    if(first == last) // We are in a leaf id, responsible of one single element
        tree[id].sum += add_val;
    else {
        int mid = (first + last) / 2;
        if(first <= pos and pos <= mid) // If pos is in the left child, recurse on the left child
            update_element(2*id, first, mid, pos, add_val);
        else // if pos is in the right child, recurse on the right child
            update_element(2*id+1, mid+1, last, pos, add_val);
        // Internal node id is responsible of an interval which is the disjoint union of those of its children
        tree[id].sum = tree[2*id].sum + tree[2*id+1].sum;
    }
}

int main () {
  cin >> n;
  for(int i = 1; i <= n; i++)
    cin >> vec[i];

  segmentation_tree_init(1, 1, n);

  cout << "survived" << endl;

  for(int i = 1; i <= n; i++)
    for(int j = i; j <= n; j++)
      cout << get_sum(1, 1, n, i, j) << endl;

  int pos = 2, increment = 10;
  update_element(1, 1, n, pos, increment);
  
  for(int i = 1; i <= n; i++)
    for(int j = i; j <= n; j++)
      cout << get_sum(1, 1, n, i, j) << endl;
    
  return 0;
}  
