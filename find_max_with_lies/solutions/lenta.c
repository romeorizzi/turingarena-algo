void individua(int n, int maxLies) {
    int i, j, max_so_far = 0;
    for(i = 1; i < n; i++) {
      int majority_vote = 0;
      for(j = 1; j <= 2*maxLies +1; j++)
         majority_vote += pesa(i, max_so_far);
      if( majority_vote > 0 )   max_so_far = i;
    }
    return max_so_far;
}

