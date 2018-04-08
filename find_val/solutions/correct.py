NONE = -1

def repeated_val(n, a):
    sort(a)
    for i in range(n):
        if a[i] == a[i-1]: 
            return a[i]
    return NONE
