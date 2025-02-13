print("Enter 1 for checking Odd or Even number")
print("Enter 2 for checking Positive or Non Positive Number")
print("Enter 3 for Simple Interest")
print("Enter 4 for Finding roots for quadratic equation")
x=int(input())
match x:
    case 1:
        x=int(input("Enter any number\n"))
        if x%2==0:
            print("Even Number")
        else:
            print("Odd Number")
    case 2:
        x=int(input("Enter any number\n"))
        if x>0:
            print("Positive Number")
        else:
            print("Non Positve Number")
    case 3:
        p,r,t=int(input("Enter the principle amount")),int(input("Enter the rate")),int(input("Enter the time(in Years"))
        SI=(p*r*t)/100
        print("Simple Interest is=",SI)
    case 4:
        print("Enter the value of a,b,c\n")
        a,b,c=int(input()),int(input()),int(input())
        d=b**2-4*a*c
        if d>=0:
            print("Real and distinct root")
        else:
            print("Imaginary Roots")