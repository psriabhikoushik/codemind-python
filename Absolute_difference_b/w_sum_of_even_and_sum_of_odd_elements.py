n=int(input())
a=list(map(int,input().split()))
s=0
k=0
for i in range(n):
    if a[i]%2==0:
        s+=a[i]
    else:
        k+=a[i]
print(abs(s-k))        