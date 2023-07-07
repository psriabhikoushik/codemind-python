def us(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

d=int(input())
m=int(input())
p=0
for i in range(d,m+1):
    if us(i)==True:
        p+=1
print(p)        