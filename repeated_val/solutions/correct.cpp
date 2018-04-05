#include <algorithm>

const int NONE = -1;

int repeated_val(int n, int* a) {
  std::sort(a, a + n);
  for(int i = 1; i < n; i++)
     if(a[i] == a[i-1])
       return a[i];
  return NONE;
}
