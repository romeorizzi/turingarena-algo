Decide whether two numbers <param>a</param> and <param>b</param> are coprime or not.

Allocate these global instance variables:

int a, b, gcd, x, y, a_and_b_coprime;

Then the values for a and b will be offered to you through a call to:

procedure set_a_and_b(a_, b_);

followed by a call to:

procedure do_the_hard_computations();

It is in this last procedure that you should get prepared to provide all answers by means of the functions.
Notice that function gimme_nontrivial_divisor() can be called only in case a and b have a common divisor greater than 1.

