// evaluation_assert not data["goals"]["correct"]
// evaluation_assert all("time limit exceeded" in line for line in stdout)

int set_a_and_b(int a_, int b_) {
    for(;;);
}

void do_the_hard_computations() {
  assert(a > 0); assert(b > 0);
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
