#include<cassert>
//#include<algorithm>
#include<bits/stdc++.h>
using namespace std;

const int NONE = -1;

int N;
vector< pair <int,int> > db; // our internal database for storing the values and answering the queries

static bool lex_sort_first_sec(const pair<int,int> &a, const pair<int,int> &b) {
   if(a.first < b.first) return true;
   if(a.first > b.first) return false;
   return (a.second < b.second);
}

void store_list(int n, int *lista_vals) {
   N = n;
   for (int i=0; i<N; i++)
       db.push_back( make_pair(arr[i],arr1[i]) ); 
   //cout << "The input database is:\n";
   //for (int i=0; i<n; i++)
   //    cout << db[i].first << " " << db[i].second << endl;

   sort(db.begin(), db.end(), lex_sort_first_sec);
   //cout << "The sorted database is:\n";
   //for (int i=0; i<N; i++)
   //    cout << db[i].first << " " << db[i].second << endl;
}

int find_val(int val) {
   if(a[0].first == val) return a[0].second;
   if(a[0].first > val) return NONE;
   if(a[N-1].first < val) return NONE;
   int left_smaller = 0;
   int right_not_smaller = N-1;
   while(left_smaller +1  < right_not_smaller) {
      assert(a[left_smaller].first < val);
      assert(a[right_not_smaller].first >= val);
      assert(left_smaller < right_not_smaller);
      int med = (left_smaller + right_not_smaller)/2;
      assert(left_smaller < med);
      assert(med < right_not_smaller);
      if(a[med].first < val)
	 left_smaller = med;
      else
	 right_not_smaller = med;
   }
   assert(left_smaller +1 == right_not_smaller);
   if(a[right_not_smaller].first == val)
      return a[right_not_smaller].second;
   else return NONE; 
}



