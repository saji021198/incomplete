nil=list(map(int,input().split()))
k=nil[len(nil)-1]
l=[j for j in input().split()]
for j in l:
    if l.count(j)==k:
        print(j)
        break
