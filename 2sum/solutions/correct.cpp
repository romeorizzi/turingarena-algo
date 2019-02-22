#include <algorithm>

const int MAXN = 200000;
int N;
int *my_val;
//int my_val[MAXN];

void store_the_numbers(int n, int* val) {
  N = n;
  my_val = (int *)malloc(N * sizeof (int));  
  for(int i = 0; i < N; i++)
    my_val[i] = val[i];
  std::sort(my_val, my_val + N);
}

void deliver_pair(int small, int big);

void list_the_pairs_of_numbers_with_sum(int SUM) {
  int pos_sml = 0, pos_big = N-1;
  while( pos_sml < pos_big ) {
    int sum = my_val[pos_sml] +  my_val[pos_big];
    if(sum < SUM)
      pos_sml++;
    else if(sum > SUM)
      pos_big--;
    else {
      deliver_pair(my_val[pos_sml], my_val[pos_big]);
      pos_sml++;
      pos_big--;
    }   
  }  
}  
