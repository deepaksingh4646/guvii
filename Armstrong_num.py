import math as m
n=int(input())
k=n
s=0
while n>9:
    r=n%10
    n=n//10
    s=s+m.pow(r,3)
s=int(s+m.pow(n,3)) 
if k==s:
    print("yes")
else:
    print("no")
