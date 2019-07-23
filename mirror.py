p=int(input())
ly=list(map(int,input().split()))
my=list(map(int,input().split()))
if(my==ly[::-1]):
    print("yes")
else:
    print("no")
