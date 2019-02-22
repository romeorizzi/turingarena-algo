#include<cassert>
#include<cstdlib>
#include<vector>

std::vector<int> prova;

// callback functions:
void cycle(int v);
void first_topological_sort(int v);
void second_topological_sort(int v);


const int MAXN = 100;
std::vector<int> out_neighbors_of[MAXN +1]; //we add a sentinel node 0, universal source
int open[MAXN +1], close[MAXN +1], t = 0;

int node_in_pos[MAXN +1], posW; // this posW gets initialized to n
int stack_cycle[MAXN +1], pos_c = 0;
bool output_delivered = false;

void dfs(int v) {
  if(open[v]) {
    if(close[v] > 0)
      return;
    else { // there is a cycle (inconsistent comparisons)
      stack_cycle[pos_c++] = v;
      return;
    }
  }  
  open[v] = ++t;
  for(int head : out_neighbors_of[v] ) {
    dfs(head);
    if(output_delivered) // cycle found and already delivered
      return;
    if(pos_c > 0) { // cycle found, rewinding up the recursion
      stack_cycle[pos_c++] = v;
      if(v == stack_cycle[0]) {
	while(pos_c > 0)
	  cycle(stack_cycle[--pos_c]);
	output_delivered = true;
      } 
    }
  }  
  close[v] = ++t;
  node_in_pos[posW--] = v; 
}  

void process_comparisons(int n, int* a, int* b) {
  posW = n; // the topological order il layed down backwards.
  int out_degree[MAXN +1];
  for(int v = 1; v <= n; v++)
    out_degree[v] = 0;
  for(int i = 0; i<n-2; i++) {
    out_neighbors_of[a[i]].push_back(b[i]);
    out_degree[a[i]]++;
  }  
  for(int v = 1; v <= n; v++)
    out_neighbors_of[0].push_back(v); // node 0 is made the universal source
  out_degree[0] = n;

  dfs(0);

  if(output_delivered)
    return;

  // If we got here, then dfs has found no cycle.
  // Indeed, the graph is acyclic as certified by the topological sort
  // encoded in vector node_in_pos[MAXN+1]

  assert( node_in_pos[0] == 0 ); // node 0 is the universal source
  int first_sink = 0; // node 0 cannot be a sink
  for(int pos = 1; pos <= n; pos++) { // just skip the dummy node 0
    first_topological_sort(node_in_pos[pos]);
    if(first_sink == 0 && out_degree[node_in_pos[pos]] == 0)
	first_sink = node_in_pos[pos];
    else
	second_topological_sort(node_in_pos[pos]);
  }  
  second_topological_sort(first_sink);
}
