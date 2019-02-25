#include <algorithm>
#include <vector>

using namespace std;

bool compare_for_pairs(const pair<int, int>&i, const pair<int, int>&j) {
  return i.second > j.second;
}


void dfs(int node, int n, int m, int *father, int *first_child, int *next_brother, void open_root_node(int s), void open_child_node(int s), void give_leaf_node(int elem), void close_node(int s), void lay_down_element(int elem), void open_set(int s), void close_set(int s)) {
  if(node > m && node != m+n) {
    give_leaf_node(node);
    lay_down_element(node);
    return;
  }
  if(node < m) {
    open_set(node);
    if(father[node] == m+n)
      open_root_node(node);
    else 
      open_child_node(node);
    for(int child = first_child[node]; child != -1; child = next_brother[child])
      dfs(child, n, m, father, first_child, next_brother, open_root_node, open_child_node, give_leaf_node, close_node, lay_down_element, open_set, close_set);
    close_node(node);
    close_set(node);
  }
}

    
int is_laminar_family(int n, int m, int *card, int **set_elem, void give_bad_pair_of_sets(int s1, int s2), void open_root_node(int s), void open_child_node(int s), void give_leaf_node(int elem), void close_node(int s), void lay_down_element(int elem), void open_set(int s), void close_set(int s), void minimal_including_set(int s, int s_big)) {
  int father[m+n+1]; // minimal including set (is unique for laminar families)
  int first_child[m+n+1],last_child[m+n+1], next_brother[m+n+1]; // to structure an ordered tree rooted at m+n
  for(int i = 0; i<=m+n; i++) {
    father[i] = m+n; // we added the whole universe as a dummy set and node (the root)
    first_child[i] = -1;
  }
  vector< pair<int, int> > the_sets;
  for(int j = 0; j<m; j++) {
    the_sets.push_back(make_pair(j,card[j]));
  }      
  sort(the_sets.begin(),the_sets.end(),compare_for_pairs);

  for(int j = 0; j<m; j++) {
    int set = the_sets[j].first;
    father[set] = father[set_elem[set][0]];
    if(first_child[father[set]] == -1) {
      first_child[father[set]] = last_child[father[set]] = set;
    }
    else {
      next_brother[last_child[father[set]]] = set;
      last_child[father[set]] = set;
    }
    for(int i = 0; i<card[set]; i++) {
      if(father[set_elem[set][i]] != father[set]) {
	give_bad_pair_of_sets(set, father[set]);
	return 0;
      }
      father[m+set_elem[set][i]] = set;
    }
  }

  for(int i = 0; i<n; i++) {
    if(first_child[father[m+i]] == -1) {
      first_child[father[m+i]] = last_child[father[m+i]] = m+i;
    }
    else {
      next_brother[last_child[father[m+i]]] = m+i;
      last_child[father[m+i]] = m+i;
    }
  }

  for(int i = 0; i < m+n; i++)
    minimal_including_set(i, father[i]);

  dfs(m+n, n, m, father, first_child, next_brother, open_root_node, open_child_node, give_leaf_node, close_node, lay_down_element, open_set, close_set);

  return 1;
}
