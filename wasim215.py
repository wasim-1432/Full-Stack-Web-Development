for n in range(15,46,1):
    for j in range(2,n+1,1):
        if n%j==0:
            break
    if n==j:
        print(n)