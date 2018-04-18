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

int binary_search(int e, int *v, int n, int(*function)(int, int) ) {
  int left = 0, right = n;
// returns the smallest index j in [0,n) such that element e is smaller than element v[j]
// returns n if no such index exists.
  while(right > left) {
     int med = (left+right)/2;
     if(smaller_assuming_min_is_MY_MIN(i,v[med]))
       right = med;
     else
       left = med+1;
  }   
  return right;
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
  vec[0]=0;
  for(int i = 1; i<n; i++) {
    int pos_ins = binary_search(i, vec, i, smaller_assuming_min_is_MY_MIN);
    for(int j = i; j>pos_ins; j--) {
      vec[j] = vec[j-1];
    }
    vec[pos_ins] = i;
  }  
  return vec[n/2];
}

