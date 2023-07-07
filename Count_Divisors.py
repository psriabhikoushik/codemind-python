a,b,c=map(int,input().split())
r=0
for i in range(a,b+1):
    if i%c==0:
        r+=1
print(r)        