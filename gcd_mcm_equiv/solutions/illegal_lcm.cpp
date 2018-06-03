// evaluation_assert not data["goals"]["lcm2gcd_legal"]
// evaluation_assert data["goals"]["gcd2lcm_legal"]
// evaluation_assert not data["goals"]["lcm2gcd_correct_always"]
// evaluation_assert data["goals"]["gcd2lcm_correct_always"]
// evaluation_assert data["goals"]["gcd2lcm_correct_for_positive_a_and_b"]

#include<cassert>  // this line should be already there in the template

int oracle_gcd(int a, int b);
int oracle_lcm(int a, int b);

int lcm(int a, int b) { // not allowed. Would cheat away the exercise.
  return oracle_lcm(int a, int b);
}

int gcd(int a, int b) {
  assert( (a >= 0) && (b >= 0) );  // this line should be already there in the template
  if(b==0)
    return a;
  return (a*b)/oracle_lcm(a, b);
}



