a=int(input())
b=int(input())
for i in range(a,b+1):
    t=i
    c=0
    while i>0:
        r=i%10
        if r==0:
            c+=1
        elif t%r!=0:
            c+=1
        i=i//10
    if c==0:
        print(t,end=' ')