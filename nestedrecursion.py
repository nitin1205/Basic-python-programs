def fun(n):
    if(n>100):
        return n-10
    return fun(fun(n+11))

r = fun(9)
print(r)