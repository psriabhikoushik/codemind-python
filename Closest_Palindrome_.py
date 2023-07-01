def abhi(m):
    n=str(m)
    n=n[::-1]
    n=int(n)
    if m==n:
        return True
    else:
        return False
n=int(input())
t=n
th=n
while True:
    n+=1
    if abhi(n)==True:
        next=n
        break
while True:
    t-=1
    if abhi(t)==True:
        p=t
        break
if abs(th-next)<abs(th-p):
    print(next)
elif abs(th-next)>abs(th-p):
    print(p)
elif abs(th-next)==abs(th-p):
    print(p,next)