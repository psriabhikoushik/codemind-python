n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    s+=a[i]
    if s//n==i:
        print(True)
        break
else:
    print(False)