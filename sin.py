import math
p=int(input())
k=p*((math.pi)/180)
j=math.sin(k)
k=int(j)
if(j<1 and j>0):
    print(round(j,1))
else:
    print(round(j))

