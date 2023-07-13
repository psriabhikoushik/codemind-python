n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in range(n):
    if i%2==0:
        s+=a[i]
for j in range(n):
    if j%2!=0:
        c+=a[j]
print(abs(s-c))