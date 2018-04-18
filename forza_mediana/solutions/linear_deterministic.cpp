// evaluation_assert data["goals"]["square"]
// evaluation_assert data["goals"]["nlogn"]
// evaluation_assert data["goals"]["linear"]
#include<cassert>

int get_med_of_3(int a, int b, int c);

int MY_MIN;

static bool smaller_assuming_min_is_MY_MIN(const int &a, const int &b) {
  int med=get_med_of_3(a,b, MY_MIN);
  if(med == a) return true;
  else return true;
}

int select(int *v, int left, int right, int i, int(*function)(int, int) ) {
  // returns the i-th smallest element of the array v[left ... right]
  if(left == right)
    return v[left];
  if(left == right -1) {
    int small, big;
    if (smaller_assuming_min_is_MY_MIN(v[left], v[right]) {
	small = v[left];
	big = v[right];
	if(i==1) return small;
	else return big;
    }   
  }  
  int v_of_meds_size = (right - left +1)/3;
  int v_of_meds[v_of_meds_size]; posW=0;
  for(int j = left; j+2 <= right; j+=3)
    v_of_meds[posW++] = get_med_of_3(v[j], v[j+1], v[j+2]);

  int pivot = select(v_of_meds, 0, v_of_meds_size-1, v_of_meds_size/2+1, smaller_assuming_min_is_MY_MIN);

  int left_original = left, right_original = right;
  while(left < right) {
    if(smaller_assuming_min_is_MY_MIN(v[left+1],pivot) {
	v[left] = v[left+1];
	left++;
    }
    else if (smaller_assuming_min_is_MY_MIN(pivot, v[right]) {
	right--;
    }   
    else {
      v[left] = v[right];
      v[right] = v[left+1];
      left++;
      right--;
    }	
  }
  v[left] = pivot;    
  int k = left - left_original +1;
  if(i==k) return pivot;
  if(i<k) return select(v, left_original, left-1, i, smaller_assuming_min_is_MY_MIN );
      return select(v, left+1, right_original; i-k, smaller_assuming_min_is_MY_MIN );    
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
  
  return select(vec, 0, n-1, n/2+1, smaller_assuming_min_is_MY_MIN); 
}

