def Find_Greater_Among_Three_Numbers(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
print("Enter any three numbers")
a,b,c=int(input()),int(input()),int(input())
print("Greatest number is=",Find_Greater_Among_Three_Numbers(a,b,c))