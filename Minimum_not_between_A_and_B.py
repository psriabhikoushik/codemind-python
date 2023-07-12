n=input()
a=list(map(int,input().split()))
c,d=map(int,input().split())
s=0
t=[]
for i in range(len(a)):
    if a[i]<c or a[i]>d:
        t.append(a[i])
        s=1
if s==0:
    print(-1)
else:
    print(min(t))