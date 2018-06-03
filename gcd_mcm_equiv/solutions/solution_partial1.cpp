// evaluation_assert data["goals"]["lcm2gcd_legal"]
// evaluation_assert data["goals"]["gcd2lcm_legal"]
// evaluation_assert data["goals"]["lcm2gcd_correct_always"]
// evaluation_assert data["goals"]["gcd2lcm_correct_for_positive_a_and_b"]
// evaluation_assert not data["goals"]["gcd2lcm_correct_always"]

#include<cassert>  // this line should be already there in the template

// Reducing the problem lcm to the problem gcd:  // would be good if we could prescribe the presence of comments like this one in the template (regardless from the target language)

int oracle_gcd(int a, int b);

int lcm(int a, int b) {
  assert ( ( (a > 0) && (b > 0) ) || ( (a == 0) && (b == 0) ) );  // this line should be already there in the template
  if(a==0)
    return 0;
  return (a*b)/oracle_gcd(a, b);
}

// Proving that the two problems are actually equivalent:

// Reducing the problem gcd to the problem lcm:

int oracle_lcm(int a, int b);

int gcd(int a, int b) {
  assert( (a >= 0) && (b >= 0) );  // this line should be already there in the template
  if(b==0)
    return a;
  return (a*b)/oracle_lcm(a, b);
}


