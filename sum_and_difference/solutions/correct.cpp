// evaluation_assert data["goals"]["correct"]
#include<cassert>

int biggest_of_two_different_naturals_with_given_sum_and_difference(int sum, int dif) {
  /*
     do there exists two different naturals A and B such that:
       1.  A+B = sum, and
       2. |A-B| = dif
     ? Yes or no? It will depend on the values of the parameters sum and dif. 
     If yes, this function should return the biggest among A and B.
     Otherwise, it should return -1.
  */

  if(dif < 1) return -1; // A and B should differ, hence dif should be positive 
  int big, small; // the two unknown numbers, with say big=max(A,B), small=min(A,B)
  /*
  big + small = sum  (+)
  big - small = dif
  _______________
 2big         = sum+dif

  -->  big = (sum + dif)/2  
  */
  big = (sum + dif)/2; // integer division, something could go wrong, a round down could occur.
  small = sum - big;
  assert(small + big == sum);
  bool check = (small + dif == big);  // the two numbers should be integers, this is not the case when (actually, iff) the round down occured
  check &= (small < big); // the two numbers should differ
  check &= (small >= 0); // the two numbers should be naturals, that is, non-negative integers
  if(check)
    return big;
  else
    return -1;
}  
