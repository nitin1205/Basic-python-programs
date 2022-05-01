def fun1(n):
    if(n>0):
        return fun1(n-1)+n
    return 0
x=0
def fun2(n):
    global x
    if(n>0):
        x+=1
        return fun2(n-1)+x
    return 0

a=fun1(5)
print(a)
b=fun2(5)
print(b)