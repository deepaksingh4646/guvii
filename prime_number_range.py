n=list(map(int,input().split()))

a=n[0]
b=n[1]
for j in range(a,b+1):
    x=0
    for i in range(2,j//2+1):
           if j%i==0:    
                x+=1
    if x==0:
        print(j,end=" ")
 