x=list(map(int,input().split()))

a=list(map(int,input().split()))
s=0
for i in range(0,x[1]):
    s=s+a[i]
print(s)