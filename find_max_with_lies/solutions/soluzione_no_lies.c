void individua(int n, int maxLies) {
    int i, max_so_far = 0;
    for(i = 1; i < n; i++)
      if( pesa(i, max_so_far) )
        max_so_far = i;
    return max_so_far;
}

