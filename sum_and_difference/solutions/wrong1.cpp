#include<cassert>

int biggest_of_two_different_naturals_with_given_sum_and_difference(int sum, int dif) {
  if(dif < 1) return -1; 
  int big = (sum + dif)/2;
  int small = sum - big;
  bool check = (small < big); // the two numbers should differ
  check &= (small >= 0); // the two numbers should be naturals, that is, non-negative integers
  if(check)
    return big;
  else
    return -1;
}  
