n=int(input())
t=n
s=0
k=str(n)
q=len(k)
while n>0 and q>=1:
    r=n%10
    s+=r**q
    n=n//10
    q-=1
if s==t:
    print(True)
else:
    print(False)