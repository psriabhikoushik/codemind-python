n=int(input())
a=list(map(int,input().split()))
k=[]
k1=[]
g=0
for i in range(len(a)):
    if a[i]%2==0:
        k.append(a[i])
    else:
        k1.append(a[i])
c=(k+k1)
print(*c)

