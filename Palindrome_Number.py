n=int(input())
for i in range(n):
    t=input()
    s=t[::-1]
    if t==s:
        print(True)
    else:
        print(False)