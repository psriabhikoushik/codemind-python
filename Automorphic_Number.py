n=int(input())
o=n
t=n**2
con=0
while n>0:
    r=n%10
    con+=1
    n=n//10
h=t%(10**con)
if h==o:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")