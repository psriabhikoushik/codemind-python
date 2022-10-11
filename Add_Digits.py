n=int(input())
s=con=y=0
while n>0:
    r=n%10
    s+=r
    n=n//10
while s>0:
    m=s%10
    con+=m
    s=s//10
while con>0:
    t=con%10
    y+=t
    con=con//10
print(y)    