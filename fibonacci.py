n=int(input())
l=[0,1]
for i in range(2,n):
    sum=l[i-1]+l[i-2]
    l.append(sum)
for i in range(0,n):
    print(l[i],end=' ')