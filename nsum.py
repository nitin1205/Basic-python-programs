#using formula
def sumA(n):
    return n*(n+1)/2


#using loop
def sumB(n):
    s=0
    for i in range(n+1):
        s+=i
    return s

#using recursion
def sumC(n):
    return sumC(n-1)+n

#print(sumA(5))
#print(sumB(5))
print(sumC(5))