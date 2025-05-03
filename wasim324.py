def Calculate_Compound_Interest(P,r,n,t):
    s=(1+r/n)**(n*t)
    A=P*s
    return A-P
print("Enter the value of p,r,n & t")
p,r,n,t=int(input()),int(input()),int(input()),int(input())
print("Compound interest is=",Calculate_Compound_Interest(p,r,n,t))