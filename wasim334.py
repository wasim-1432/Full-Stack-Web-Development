def Check_Prime_Number_Or_Not(n):
    i=2
    while i<=n:
        if n%i==0:
            break
        i+=1
    if n==i:
        return True
    else:
        return False
n=int(input("Enter any number\n"))
print("Required answer is=",Check_Prime_Number_Or_Not(n))