n=int(input("Enter any number\n"))
prime=[]
k=2
while k<=n:
    i=2
    while i<=k:
        if k%i==0:
            break
        i+=1
    if i==k:
        prime.append(k)
    k+=1
print(prime)