n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)):
    if a[i]%2==0:
        c+=1
    else:
        print(False)
        break
if c==len(a):
    print(True)