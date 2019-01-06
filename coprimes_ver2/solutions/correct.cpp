// evaluation_assert data["goals"]["correct"]
// evaluation_assert not data["goals"]["efficient"]
#include <cassert>

const int YES = 1;
const int NO = 0;

int a, b, gcd, x, y, a_and_b_coprime;

void set_a_and_b(int a_, int b_) {
  assert(a_ > 0); assert(b_ > 0);
  a = a_;
  b = b_;
}

void recEuclide(int a, int b, int answ[3]) {
  /* returns the answ array [d,x,y] where:
       d is the greatest divisor of a and b;
       x and y are integers such that  xa + yb = d.
  */  
  assert(a >= 0); assert(b >= 0); assert(a + b > 0);
  if(b > a) {
    int rec_answ[3];
    recEuclide(b,a, rec_answ);
    answ[0] = rec_answ[0]; answ[1] = rec_answ[2]; answ[2] = rec_answ[1];
    return;
  }
  assert(a >= b); assert(b >= 0); assert(a > 0);    
  if( (b == 0) || (a == b) ) {
    answ[0] = a; answ[1] = 1; answ[2] = 0;
    return;
  }    
  int A = a;
  int q = A / b;
  a = A % b;
  int rec_answ[3];
  recEuclide(a,b, rec_answ);
  //    A = bq + a
  //    xa + yb = 1
  //    xA +(y-xq)b= xbq + xa +yb -xqb
  answ[0] = rec_answ[0]; answ[1] = rec_answ[1]; answ[2] = rec_answ[2]-rec_answ[1]*q;
}

void do_the_hard_computations() {
  assert(a > 0); assert(b > 0);
  int answ[3];
  recEuclide(a,b, answ);
  gcd = answ[0]; x = answ[1]; y = answ[2];
  if(gcd == 1) 
    a_and_b_coprime = YES;
  else
    a_and_b_coprime = NO;
}

int gimme_a() {
  return a;
}

int gimme_b() {
  return b;
}

int are_a_and_b_coprime() {
  return a_and_b_coprime;
}

int gimme_nontrivial_divisor() {
  assert(gcd > 1);
  return gcd;
}

int gimme_a_multiplier() {
  return x;
}

int gimme_b_multiplier() {
  return y;
}
