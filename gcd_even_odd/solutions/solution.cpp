int sum(int a, int b);
int dif(int a, int b);
int is_odd(int a);
int half_of(int a);

int gcd() {
  if( a_is_even() && b_is_even() ) {
    halve_a(); halve_b();
    return 2*gcd();
  }  
  while( a_is_even() )
    halve_a();
  assert( !a_is_even() );
  while( b_is_even() )
    halve_b();
  assert( !b_is_even() );
  
  take_sum_and_dif_of_a_and_b_as_new_a_and_b(); 
  assert( a_is_even() ); assert( b_is_even() );

  return gcd();
}


