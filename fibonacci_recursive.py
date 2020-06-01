def f(n):
    if(n==1 or n ==0) :
        return n
    while(n>0):
            x= f(n-1) + f(n-2)
            return x

n=7
t = f(n)
print("T :",t)
