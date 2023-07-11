n=input()
a=list(map(int,input().split()))
b,c=map(int,input().split())
s=0
l=[]
for i in range(len(a)):
    if a[i]>=b and a[i]<=c:
        l.append(a[i])
        s=1
if s==0:
    print(-1)
else:
    print(max(l))