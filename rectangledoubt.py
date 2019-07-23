ko,lo=map(int,input().split())
y=[(i,j) for i in range(ko) for j in range(lo) if i+j==(ko/2) and i*j==lo]
if len(y)>0:
    print("yes")
else:
    print("no")    
