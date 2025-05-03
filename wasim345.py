def Print_All_Factors_Of_A_Given_Number(n):
    i=1
    while i<=n:
        if n%i==0:
            print(i,end=' ')
        i+=1
n=int(input("Enter any number\n"))
Print_All_Factors_Of_A_Given_Number(n)