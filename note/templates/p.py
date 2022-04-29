import math
t=int(input())
count=0
while t>0:
    l,r=map(int,input().split(" "))
    for i in range(l,r+1):
        b=math.sqrt(i)
        if int(b)==math.ceil(b):
            continue
        if i==1:
            continue
        flag=0
        for j in range(4,i//2+1):
            if i%j==0:
                b=math.sqrt(j)
                if int(b)==math.ceil(b):
                    flag=1
                    break
        if flag==0:
            count+=1
    print(count)
    t=t-1
