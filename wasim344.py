def Print_First_N_Terms_Of_Fibonacci_Series(n):
    a=-1
    b=1
    s=0
    while s<=n:
        s=a+b
        if s>=n:
            break
        print(s,end=' ')
        a=b
        b=s
        s+=1
n=int(input("Enter any number\n"))
Print_First_N_Terms_Of_Fibonacci_Series(n)