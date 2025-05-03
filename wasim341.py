def Print_First_N_Odd_Natural_Numbers(n):
    i=1
    while i<=n:
        print(2*i-1,end=' ')
        i+=1
n=int(input("Enter any numbers\n"))
Print_First_N_Odd_Natural_Numbers(n)