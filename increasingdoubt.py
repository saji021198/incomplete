y=int(input())
p=list(map(int,input().split()))
countone=1
counttwo=1
for i in range(0,y-1):
     if(p[i]<(p[i+1])):
         countone=countone+1
         counttwo=1
     else:
         for j in range(i+1,y-1):
             if(p[j]<(p[j+1])):
                 counttwo=counttwo+1
                 countone=1
         else:
             break
if(countone>counttwo):
    print(countone)
else:
    print(counttwo)
