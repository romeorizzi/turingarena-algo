#include<cassert>
#include<iostream>
#include<vector>

using namespace std;

const int MAX_N = 100000;
int n, m;
vector<int> exiting[MAX_N+1], entering[MAX_N+1];

int node_in_pos[MAX_N+1], num_placed = 0;
int max_length_path_starting_from_node[MAX_N+1], out_degree[MAX_N+1], removed[MAX_N+1];
int posRW = 0, stack_of_sink_nodes[MAX_N];

int main() {
  cin >> n >> m;
  for(int i = 0; i<m;i++) {
    int tail, head;
    cin >> tail >> head;
    exiting[tail].push_back(head);
    entering[head].push_back(tail);
    out_degree[tail]++;
  }  

  for(int v = 1; v <= n; v++)
    if(out_degree[v] == 0)
      stack_of_sink_nodes[posRW++] = v;

  while(posRW > 0) {
    int s = stack_of_sink_nodes[--posRW];
    node_in_pos[n-num_placed++] = s;
    removed[s] = 1;
    for( int v : entering[s] )
      if(--out_degree[v] == 0)
	stack_of_sink_nodes[posRW++] = v;
  }
  /*
  cerr << endl << "num nodes removed: " << num_placed << endl;
  cerr << endl << "They where removed as sinks in the following order: " << num_placed << endl;
  for(int i = 0; i < num_placed; i++)
    cerr << node_in_pos[n-i] << " ";
  cerr << endl;
  */
  
  if(num_placed < n) {  // we are left with some nodes but no one of these is now a source -> there must be a cycle
    cout << -1 << " "; // there must be a cycle, we now search for it ...
    int visited[MAX_N +1], nxt[MAX_N +1];
    for(int i = 1; i <= n; i++)  visited[i] = 0; // no node visited yet
    int v = 1; while( removed[v] )  v++;  // place the pebble in any unremoved v
    while( !visited[v] ) {
      //cerr << "visit node " << v << endl; 
      visited[v] = 1;
      for( int next : exiting[v] )
        if( !removed[ next ] ) {
          nxt[v] = next;
          //cerr << "the pebble could move to " << next << endl;
	}  
      v = nxt[v];
    }
    int u = v; //we got back to an already visited node v, we flag it in u, and now go for another round ... 
    int len = 0;
    do {
      len++;
      v = nxt[v];
    } while( v != u );
    cout << len << endl;
    // and again...
    do { // and print the nodes one by one
      cout << v << " "; // cout << v << " ";
      v = nxt[v];
    } while( v != u );
    cout << endl;
  }
  else {
    int max_so_far = 0, good_start, nxt[MAX_N +1];
    for(int pos = n-1; pos >= 0; pos--) {
      int node = node_in_pos[pos];
      max_length_path_starting_from_node[node] = 1;
      int best_future = 0;
      for( int next : exiting[node] )
	if(best_future < max_length_path_starting_from_node[next]) {
           best_future = max_length_path_starting_from_node[next];
	   nxt[node]=next;
	}   
      max_length_path_starting_from_node[node] += best_future;
      if(max_so_far < max_length_path_starting_from_node[node]) {
         max_so_far = max_length_path_starting_from_node[node];
	 good_start = node;
         // cerr << "max_length_path_starting_from_node[" << node << "] = " << max_length_path_starting_from_node[node] << endl;
      }	 
    }
    cout << max_so_far << endl;  // max length of a path in the removed nodes
    int v = good_start;  // good_start = the first node of a maximum length path
    while( v ) {  // we print the nodes one by one
      cout << v << " ";
      v = nxt[v];   // nxt[] was properly set up during the dyn programming 
    }
    cout << endl;
  }
  return 0;
}
