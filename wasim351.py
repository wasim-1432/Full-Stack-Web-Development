def Calculate_LCM_Of_Two_Given_Numbers(a,b):
    i,s=2,1
    while a!=1 or b!=1:
        if a%i==0 and b%i==0:
            a=a/i
            b=b/i
            s=s*i
            continue
        elif a%i==0:
            a=a/i
            s=s*i
            continue
        elif b%i==0:
            b=b/i
            s=s*i
            continue
        i+=1
    return s
print("Enter any two numbers")
a,b=int(input()),int(input())
print("LCM is=",Calculate_LCM_Of_Two_Given_Numbers(a,b))