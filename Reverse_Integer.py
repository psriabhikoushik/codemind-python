n=int(input())
f=abs(n)
s=0
if n>0:
    while n>0:
       r=n%10
       s=s*10+r
       n=n//10
    print(s)
else:
    while f>0:
       r=f%10
       s=s*10+r
       f=f//10
    print(-(s))