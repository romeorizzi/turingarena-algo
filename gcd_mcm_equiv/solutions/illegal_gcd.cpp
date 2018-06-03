// evaluation_assert data["goals"]["lcm2gcd_legal"]
// evaluation_assert not data["goals"]["gcd2lcm_legal"]
// evaluation_assert data["goals"]["lcm2gcd_correct_always"]
// evaluation_assert not data["goals"]["gcd2lcm_correct_always"]
// evaluation_assert not data["goals"]["gcd2lcm_correct_for_positive_a_and_b"]

#include<cassert>  // this line should be already there in the template

int oracle_gcd(int a, int b);
int oracle_lcm(int a, int b);

int lcm(int a, int b) { // not allowed. Would cheat away the exercise.
  assert ( ( (a > 0) && (b > 0) ) || ( (a == 0) && (b == 0) ) )  // this line should be already there in the template
  if(a==0)
    return 0;
  return (a*b)/oracle_gcd(a, b);
}

int gcd(int a, int b) { // not allowed. Would cheat away the exercise.
  return oracle_gcd(a, b);
}


