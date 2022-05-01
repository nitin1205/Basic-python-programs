#using loop:-
def fibA(n):
    ta=0
    tb=1
    s=0
    if(n<=1):
        return n
    for i in range(2,n+1):
        s=ta+tb
        ta=tb
        tb=s
    return s

#using recursion
def fibB(n):
    if(n<=1):
        return n
    return fibB(n-2)+fibB(n-1)

#using memoization
def fibC(n):
    if(n<=1):
        a[n]=n
        return n
    else:
        if a[n-2]==-1:
            a[n-2]=fibC(n-2)
        if a[n-1]==-1:
            a[n-1]==fibC(n-1)
        return fibC(n-2)+fibC(n-1)

n=5
a=[]
for i in range(n):
    a.append(-1)
print(fibA(n))
print(fibB(n))
print(fibC(n))
