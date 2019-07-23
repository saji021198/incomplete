y=int(input())
p=list(map(int,input().split()[:y]))
l=sorted(p)
u=len(l)
kin=l[u-1]-l[0]
print(kin)
