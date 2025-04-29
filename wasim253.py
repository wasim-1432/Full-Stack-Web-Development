n=int(input("Enter a number\n"))
fib=[]
a,b=-1,1
while n:
    c=a+b
    fib.append(c)
    a=b
    b=c
    n-=1
print(fib)