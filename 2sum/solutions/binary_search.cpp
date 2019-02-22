#include <algorithm>

int N;
int *my_val;

void store_the_numbers(int n, int* val) {
  N = n;
  my_val = (int *)malloc(N * sizeof (int));  
  for(int i = 0; i < N; i++)
    my_val[i] = val[i];
  std::sort(my_val, my_val + N);
}

void deliver_pair(int small, int big);

void list_the_pairs_of_numbers_with_sum(int SUM) {
  for(int pos_sml = 0; pos_sml < N; pos_sml++)
    if(my_val[pos_sml] < SUM/2) {
      int big_addendum = SUM - my_val[pos_sml];
      int pos_big_LB = pos_sml+1, pos_big_UB = N-1;
      while(pos_big_LB <= pos_big_UB) {
	int pos_med = (pos_big_LB + pos_big_UB)/2;
	if(my_val[pos_med] == big_addendum) {
           deliver_pair(my_val[pos_sml], my_val[pos_med]);
	   pos_big_LB = pos_big_UB +1;
	}
	else if(my_val[pos_med] < big_addendum)
	   pos_big_LB = pos_med +1;
	else (my_val[pos_med] < big_addendum)
	   pos_big_UB = pos_med -1;
    }  
}  
