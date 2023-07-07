n=int(input())
r=0
w=n
while n>0:
    r1=n%10
    r=r*10+r1
    n//=10
if w==r:
    print(True)
else:
    print(False)