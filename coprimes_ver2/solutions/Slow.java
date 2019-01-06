// evaluation_assert data["goals"]["correct"]
// evaluation_assert not data["goals"]["efficient"]

class Slow extends Skeleton {
    private static final YES = 1;
    private static final NO = 0;

    void set_a_and_b(int a_, int b_) {
	assert(a_ > 0); assert(b_ > 0);
	a = a_;
	b = b_;
    }

    void do_the_hard_computations() {
	assert(a > 0); assert(b > 0);
	int  gcd = 1;
	for(int i= 2; i<a+b; i++)
	    if(a%i == 0 && b%i == 0)
		gcd = i;
	if(gcd > 1)
	    a_and_b_coprime = NO;
	else {
	    a_and_b_coprime = YES;
	    for(int y = 0; y<a; y++)
		if( (a*b+gcd - y*b) % a == 0) {
		    x = (gcd - y*b) / a;
		    return;
		}
	    // gcd = xa + yb con |x|<b e |y|<a con xy <= 0
	    // -> ab + gcd = xa +yb con x,y >= 0, x<b e y<a
	}
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

}
