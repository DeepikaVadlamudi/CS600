import time

t = time.process_time()

def ClimbingStairs(n):
    if(n<0):
        return 0
    if(n==0):
        return 1
    else:
        x = ClimbingStairs(n-1) + ClimbingStairs(n-2) +ClimbingStairs(n-3)
        return x

n =  20
a = ClimbingStairs(n)
print("A :",a)
elapsed_time = time.process_time() - t
print("time:",elapsed_time)
