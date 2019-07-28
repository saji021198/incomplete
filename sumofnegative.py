popp=int(input())
sum=0
k=list(map(int,input().split()))
for i in k:
    if(i<0):
        sum=sum+i
print(sum)
