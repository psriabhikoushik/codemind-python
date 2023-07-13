n=int(input())
a=list(map(int,input().split()))
b=int(input())
for i in range(n):
    if b in a:
        print(True)
        break
else:
    print(False)