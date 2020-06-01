#Needs a lot of modifications
#functions to be incorporated


p = [25,24,15]
w = [18, 15, 10]
n=3
s =[0.0,0.0,0.0]
for i in range(len(p)):
    s[i] = p[i]/w[i]
    print(s[i])
index = [1,2,0]
#done in accordance with S[i]
maxw = 20
U = maxw
x = [0.0, 0.0, 0.0]
for i in index:
    print("i:",i)
    if(w[i] > U):
        break
    x[i] = 1.0
    U = U - w[i]
    print("U:",U)
if(i<=n):
    x[i] = U/w[i]

profit = 0
for i in range(len(p)):
    print(x[i])
    profit += x[i]*p[i]
    print("Profit:", profit)
