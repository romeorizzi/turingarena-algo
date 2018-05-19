// evaluation_assert not data["goals"]["correct"]
// evaluation_assert data["goals"]["correct-when-different"]
#include<cassert>

int biggest_of_two_different_naturals_with_given_sum_and_difference(int sum, int dif) {
  if(dif < 1) return -1; 
  int big = (sum + dif)/2;
  int small = sum - big;
  bool check = (small + dif == big);  // the two numbers should be integers, this is not the case when (actually, iff) the round down occured
  check &= (small >= 0); // the two numbers should be naturals, that is, non-negative integers
  if(check)
    return big;
  else
    return -1;
}  
