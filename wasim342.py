def Print_First_N_Prime_Numbers(n):
    s=1
    while s<=n:
        i=2
        while i<=s:
            if s%i==0:
                break
            i+=1
        if s==i:
            print(s,end=' ')
        s+=1
n=int(input("Enter any number\n"))
Print_First_N_Prime_Numbers(n)