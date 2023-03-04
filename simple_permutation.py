def permutation(n):
    if n==1:
        return 1
    else:
        return n*(permutation(n-1))
    
print(permutation(3))
print(permutation(4))
print(permutation(5))
