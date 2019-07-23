y=int(input())
p=list(map(int,input().split()[:y]))
l=sorted(p)
u=len(l)
kin=l[1]-l[0]
print(kin)
