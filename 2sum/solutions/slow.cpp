#include <algorithm>

int N;
int *my_val;

void store_the_numbers(int n, int* val) {
  N = n;
  my_val = (int *)malloc(N * sizeof (int));  
  for(int i = 0; i < N; i++)
    my_val[i] = val[i];
}

void deliver_pair(int small, int big);

void list_the_pairs_of_numbers_with_sum(int SUM) {
  for(int pos_sml = 0; pos_sml < N; pos_sml++)
    if(my_val[pos_sml] < SUM/2) {
      int big_addendum = SUM - my_val[pos_sml];
      for(int pos_big = 0; pos_big < N; pos_big++)
	if(my_val[pos_big] == big_addendum)
           deliver_pair(my_val[pos_sml], my_val[pos_big]);
    }  
}  
