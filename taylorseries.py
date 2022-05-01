#method 1:-
p=1.0
f=1.0
def eA(x,n):
    global p
    global f
    if(n==0):
        return 1
    else:
        r=eA(x,n-1)
        p=p*x
        f=f*n
        return r+p/f

#method 2:- horner's rule
#using loop
def eB1(x,n):
    s=1.0
    num=1.0
    den=1.0
    for i in range(1,n+1):
        num*=x
        den*=i
        s+=num/den
    return s

#using recursion
s=0.0
def eB2(x,n):
    global s
    if(n==0):
        return s
    s=1+x*s/n
    return eB2(x,n-1)


a=1
b=10
print(eA(a,b))
print(eB1(a,b))
print(eB2(a,b))