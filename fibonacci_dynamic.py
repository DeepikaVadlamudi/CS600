def f(n):
    a=0
    b=1
    if(n<0):
        print("wrong input")
    if(n<=1):
        return n
    else:
        for i in range(1,n):
            x = a + b
            a = b
            b = x
        return b

d = f(7)
print("D :",d)
