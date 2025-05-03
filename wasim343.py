def Print_N_Prime_Numbers(n1,n2):
    s=n1
    while s<=n2:
        i=2
        while i<=s:
            if s%i==0:
                break
            i+=1
        if s==i:
            print(s,end=' ')
        s+=1
n1,n2=int(input("Enter first number\n")),int(input("Enter second number\n"))
Print_N_Prime_Numbers(n1,n2)