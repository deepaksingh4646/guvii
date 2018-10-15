m=int(input())
n=m
s=0
while n>9:
    r=n%10
    n=n//10
    s=s*10+r
s=s*10+n
if n==s:
    print("yes")
else:
    print("no")