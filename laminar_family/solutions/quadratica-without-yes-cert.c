#include"stdlib.h"

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int is_laminar_family(int n, int m, int *card, int **set_elem, void give_bad_pair_of_sets(int s1, int s2), void open_root_node(int s), void open_child_node(int s), void give_leaf_node(int elem), void close_node(int s), void lay_down_element(int elem), void open_set(int s), void close_set(int s), void minimal_including_set(int s, int s_big)) {
  for(int set1 = 0; set1 < m; set1++) {
    qsort(set_elem[set1], card[set1], sizeof(int),cmpfunc);
    for(int set2 = 0; set2 < set1; set2++) {
      int only_in_set1 = 0;
      int only_in_set2 = 0;
      int in_both_sets = 0;
      int j = 0;
      for(int i = 0; i<card[set1]; i++) {
	while( (j<card[set2]) && (set_elem[set2][j] <= set_elem[set2][j]) ) {
	  if(set_elem[set2][j] < set_elem[set2][j])
	    only_in_set2++;
	  if(set_elem[set2][j] == set_elem[set2][j])
	    in_both_sets++;
	  j++;
	}
	if(j<card[set2])
	  only_in_set1++;
      }
      if( only_in_set1 > 0 && only_in_set2 > 0 && in_both_sets > 0) {
	give_bad_pair_of_sets(set1, set2);
	return 0;
      }
    }
  }
  return 1;
}
