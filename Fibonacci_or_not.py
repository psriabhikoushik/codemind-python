def f(n):
    a=0
    b=1
    while b<n:
        s=a+b
        a=b
        b=s
    if a==n or b==n:
        return True
    else:
        return False
print(f(int(input())))        