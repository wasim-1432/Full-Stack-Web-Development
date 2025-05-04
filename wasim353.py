def Prime_Numbers_Between_Two_Given_Numbers(a,b):
    s=a
    l=[]
    while s<=b:
        i=2
        while i<=s:
            if s%i==0:
                break
            i+=1
        if s==i:
            l.append(s)
        s+=1
    return l
print("Enter any two numbers\n")
a,b=int(input()),int(input())
print("Prime number list is=",Prime_Numbers_Between_Two_Given_Numbers(a,b))