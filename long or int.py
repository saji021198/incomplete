now=int(input())
if(now>=-2**15+1)and(now<=2**15+1):
    print("INT")
elif(now>=-2**31+1)and(now<=2**31+1):
    print("LONG")
else:
    print("LONG LONG")
