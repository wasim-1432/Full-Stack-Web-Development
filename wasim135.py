print("Enter any three numbers")
x,y,z=int(input()),int(input()),int(input())
if x>=y and x>=z:
    print("Greater is",x)
elif y>=x and y>=z:
    print("Greater is",y)
elif z>=x and z>=y:
    print("Greater is",z)
