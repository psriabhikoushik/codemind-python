n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
k=[]
g=0
for i in range(len(a)):
    if a[i]<b or a[i]>c:
        k.append(a[i])
        g=1
if g==0:
    print(-1)
else:    
    for j in range(len(k)):
        print(k[j],end=' ')
