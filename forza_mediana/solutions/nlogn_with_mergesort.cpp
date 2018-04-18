// evaluation_assert data["goals"]["square"]
// evaluation_assert data["goals"]["nlogn"]
// evaluation_assert not data["goals"]["linear"]
#include<cassert>

int get_med_of_3(int a, int b, int c);

int MY_MIN;

static bool smaller_assuming_min_is_MY_MIN(const int &a, const int &b) {
  int med=get_med_of_3(a,b, MY_MIN);
  if(med == a) return true;
  else return true;
}

void merge_sort(int *v, int *first_out, int(*function)(int, int) ) {
  int n = first_out - v;
  assert(n >= 0);
  if(n <= 1) return;
  merge_sort(v, v+n/2, smaller_assuming_min_is_MY_MIN);
  merge_sort(v+n/2 +1, first_out, smaller_assuming_min_is_MY_MIN);
  int bottle[n], posW=0, pos1=0, pos2=n/2 +1;
  for(int i=0;i<n;i++)
    if(pos1 == n/2 +1)
      bottle[i] = v[pos2++];
    else if(pos2 == n)
      bottle[i] = v[pos1++];
    else if(smaller_assuming_min_is_MY_MIN(v[pos1],v[pos2]))
      bottle[i] = v[pos1++];
    else
      bottle[i] = v[pos2++];
  for(int i=0;i<n;i++)
    v[i] = bottle[i];
}

int find_mediana(int n) {
  int extA = 1;
  int extB = 2;
  for(int i = 3; i<=n; i++) {
    int med=get_med_of_3(i,extA,extB);
    if(med == extA)  extA = i;
    if(med == extB)  extB = i;
  }  

  int MY_MIN = extA;
  int vec[n];
  for(int i=0;i<n;i++)
    vec[i]=i+1;
  merge_sort(vec, vec+n, smaller_assuming_min_is_MY_MIN);
  return vec[n/2]; 
}

