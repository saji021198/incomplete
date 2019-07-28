p,m=map(int,input().split())
l=p+m
eu=[]
hu=[]
q=list(map(int,input().split()))
for i in range(0,p):
    for j in range(p,l):
       if(q[i]==q[j]):
           eu.append(q[i])
           break
for r in eu:
    if r in q:
        e=q.count(r)
        if(e%2!=0):
            eu.remove(r)
            for i in range(1,len(eu)):
                if(eu[0]==eu[i]):
                    i=i+1
    break

print(*eu)
