p=int(input())
uj=list(map(int,input().split()))
m=uj[0]
for i in range(1,p):
    m=m|uj[i]
print (m)
