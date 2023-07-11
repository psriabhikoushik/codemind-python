n=int(input())
s=0
p=1
rev=0
while n>0:
    c=n%10
    s+=c
    p*=c
    n=n//10
print(p-s)    