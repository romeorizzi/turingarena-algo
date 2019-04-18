#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>

using namespace std;

const int MAXN = 100000;
int n, m;
vector<int> uscente[MAXN+1];

int node_in_pos[MAXN];
int max_length_path_starting_from_node[MAXN];

int main() {
  cin >> n >> m;
  for(int i = 0; i<m;i++) {
    int a, b;
    cin >> a >> b;
    uscente[a].push_back(b);
  }  

  for(int i = 1; i <= n; i++)
    node_in_pos[i-1] = i;

  for(int pos = n-1; pos >= 0; pos--) {
    int node = node_in_pos[pos];
    max_length_path_starting_from_node[node] = 1;
    int best_future = 0;
    for( int next : uscente[node] )
      best_future = max(best_future, max_length_path_starting_from_node[next]);
    max_length_path_starting_from_node[node] += best_future;
    printf("max_length_path_starting_from_node[%d] = %d\n", node, max_length_path_starting_from_node[node]);
  }
  
  return 0;
}
