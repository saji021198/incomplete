p=int(input())
u=list(map(int,input().split()))
l=[]
mux=u[0]
for i in range(1,p):
    mux=mux|u[i]
    l.append(mux)
print (max(l))
