a,x,z=map(int,input().split())
if(a!=0 and x!=0 and z!=0):
    ani=a+x+z
else:
    ani=0
if(ani==180):
    print("yes")
else:
    print("no")
