n=int(input())
a=[]
for i in range(1,6):
    a.append(n*i)
print(*a,end=" ")