n,p=map(int,input().split())
s=n%(10**p)
re=h=0
while n>0:
    r=n%10
    re=re*10+r
    n=n//10
k=re%(10**p)
while k>0:
    l=k%10
    h=h*10+l
    k=k//10
e=(h-s)
j=abs(e)
print(j)