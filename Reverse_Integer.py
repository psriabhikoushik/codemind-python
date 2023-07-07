n=int(input())
t=abs(n)
r=0
while t>0:
    r1=t%10
    r=r*10+r1
    t=t//10
if n>0:
    print(r)
else:
    print(-(r))