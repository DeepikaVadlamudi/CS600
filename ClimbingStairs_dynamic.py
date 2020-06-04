def ClimbingStairs(n):
    a = 0
    b = 1
    c= 1
    if(n<0):
        return 0
    if(n==0):
        return 1
    if(n==1):
        return 1
    else:
        for i in range(1,n):
            x = a+b+c
            a = b
            b = c
            c = x
        return c

n = 4
s = ClimbingStairs(n)
print("S : ",s)
