lo,mo=(map(str,input().split()))
if(lo=='R' and mo=='P') or (lo=='P' and mo=='R'):
    print("P")
elif(lo=='R' and mo=='S' or lo=='S' and mo=='R'):
    print("R")
elif(lo=='S' and mo=='P' or lo=='P' and mo=='S'):
    print("S")
elif(lo==mo):
    print("D")
