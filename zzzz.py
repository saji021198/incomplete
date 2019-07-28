p,m=map(int,input().split())
l=p+m
eu=[]
hu=[]
q=list(map(int,input().split()))
for i in range(0,p):
    for j in range(p,l):
       if(q[i]==q[j]):
           eu.append(q[i])
for k in eu:
    if k not in hu:
        hu.append(k)
print(*hu)
