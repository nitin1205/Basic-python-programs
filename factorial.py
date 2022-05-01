#using loop

def factA(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s

#using recursion

def factB(n):
    if(n==0):
        return 1
    return factB(n-1)*n

print(factA(5))
print(factB(5))