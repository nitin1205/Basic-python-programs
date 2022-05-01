def fun1(n):
    if(n>0):
        print(n,end=" ")
        fun1(n-1)
def fun2(n):
    if(n>0):
        fun2(n-1)
        print(n,end=" ")
x = 3
fun1(x)
fun2(x)