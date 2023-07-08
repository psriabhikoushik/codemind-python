n=int(input())
a=list(map(int,input().split()))
s=sum(a)
d=n
while d>0:
    if s%d==0:
        print(d)
        break
    d-=1