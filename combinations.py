#calculating factorial
def fact(n):
    if(n==0):
        return 1
    return fact(n-1)*n

#using formula
def nCr(n,r):
    num=fact(n)
    den=fact(r)*fact(n-r)
    return num/den

#using recursion
def NCR(n,r):
    if(n==r or r==0):
        return 1
    return NCR(n-1,r-1)+NCR(n-1,r)


n=5
r=1
print(nCr(n,r))
print(NCR(n,r))