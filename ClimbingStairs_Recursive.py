def ClimbingStairs(n):
    if(n<0):
        return 0
    if(n==0):
        return 1
    else:
        x = ClimbingStairs(n-1) + ClimbingStairs(n-2) +ClimbingStairs(n-3)
        return x

n =  7
a = ClimbingStairs(n)
print("A :",a)
