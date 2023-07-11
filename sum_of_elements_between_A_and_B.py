n=input()
a=list(map(int,input().split()))
b,c=map(int,input().split())
s=0
for i in range(len(a)):
    if a[i]>=b and a[i]<=c:
        s+=a[i]
print(s)        