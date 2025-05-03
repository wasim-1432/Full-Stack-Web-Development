def Calculate_Factorial(n):
    s=1
    while n:
        s=s*n
        n-=1
    return s
n=int(input("Enter any number\n"))
print("Factorial is=",Calculate_Factorial(n))