def AM(n):
    c=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            c+=i
    return c


a=int(input())
b=int(input())
if b==AM(a) and a==AM(b):
    print('Amicable')
else:
    print('Not Amicable')