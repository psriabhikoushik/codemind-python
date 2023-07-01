n=int(input())
s=0
while n:
    s*=10
    s+=(n%10)
    n//=10
q=0
while s:
    n*=10
    if s%10==6 and q==0:
        n+=9
        q=1
    else:
        n+=s%10
    s//=10    
print(n)        