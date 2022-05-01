def powerA(m,n):
    if(n==0):
        return 1
    return powerA(m,n-1)*m

def powerB(m,n):
    if(n==0):
        return 1
    if(n%2==0):
        return powerB(m*m,n/2)
    return m * powerB(m*m,(n-1)/2)


print(powerA(2,9))
print(powerB(2,9))