n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
m1=(n1[0]*60)+n1[1]
m2=(n2[0]*60)+n2[1]

n=abs(m1-m2)
h=n//60
m=n-(60*h)
print(""+str(h)+" "+str(m))
