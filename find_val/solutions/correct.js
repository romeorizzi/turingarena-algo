const NONE = -1;

function repeated_val(n, a) {
  a.sort();
  for(var i = 1; i < n; i++)
     if(a[i] == a[i-1])
       return a[i];
  return NONE;
}
