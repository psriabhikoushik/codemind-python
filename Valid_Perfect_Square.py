n=int(input())
for i in range(n):
    t=int(input())
    k=(t**0.5)//1
    if k*k==t:
        print(True)
    else:
        print(False)