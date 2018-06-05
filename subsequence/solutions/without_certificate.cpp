// evaluation_assert data["goals"]["correct_yes_no"]
// evaluation_assert not data["goals"]["correct_with_certificate"]
// evaluation_assert data["goals"]["single_check_per_text_element"]

int check(int pos_p, int pos_t);
void underline(int pos_p);

int subsequence(int len_p, int len_t) {
  int pos_p = 1, pos_t = 1;
  while(pos_p <= len_p && pos_t <= len_t) {
    if( check(pos_p, pos_t) ) {
      pos_p++;
      pos_t++;      
    }
    else pos_t++;      
  }
  if(pos_p > len_p)
    return 1;
  else
    return 0;
}