n=int(input())
f=n*n
p=0
while f>0:
    c=f%10
    p+=c
    f=f//10
if p==n:
    print('Neon Number')
else:
    print('Not Neon Number')