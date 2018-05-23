int guess(int n);

int play(int n) {
    int min = 1, max = n, mid;
    while (true) {
        if ( min == max )
            return min;

        mid = (min+max)/2;
        switch ( guess(mid) ) {
            case -1: // too low
                min = mid+1;
                break;
            case 1:  // too high
                max = mid-1;
                break;
            default:  // correct
                return mid;
        }
    }
    return 1; // dummy
}

